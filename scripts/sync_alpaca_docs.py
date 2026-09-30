#!/usr/bin/env python3
"""Mirror Alpaca public US Markdown documentation and official OpenAPI specs."""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import ipaddress
import json
import logging
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import uuid
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

def atomic_write_bytes(path: Path, data: bytes) -> None:
    """Write one file atomically on the destination filesystem."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_name, path)
    except BaseException:
        try:
            os.unlink(temporary_name)
        except FileNotFoundError:
            pass
        raise

INDEX_URL = "https://docs.alpaca.markets/us/llms.txt"
SPEC_URLS = {
    "trading-api.json": "https://docs.alpaca.markets/openapi/trading-api.json",
    "market-data-api.json": "https://docs.alpaca.markets/openapi/market-data-api.json",
    "broker-api.json": "https://docs.alpaca.markets/openapi/broker-api.json",
}
LINK_RE = re.compile(r"\[[^]]+\]\((https://docs\.alpaca\.markets/us/(?:docs|reference)/[^)]+\.md)\)")
RELEVANT = (
    "authentication", "sdk", "trading", "option", "market-data", "websocket",
    "historical", "order", "rate-limit", "fix", "paper",
)
_rate_lock = threading.Lock()
_next_request_at = 0.0
_minimum_interval = 0.35


class ChineseFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        timestamp = datetime.now(UTC).isoformat(timespec="milliseconds")
        return f"时间={timestamp} 级别={record.levelname} 组件=alpaca文档同步 消息={record.getMessage()}"


def configure_logging(debug: bool) -> logging.Logger:
    logger = logging.getLogger("alpaca_docs_sync")
    logger.handlers.clear()
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(ChineseFormatter())
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG if debug else logging.INFO)
    return logger


def sha256(data: bytes) -> str:
    # Git may materialize the mirrored UTF-8 text files as CRLF on Windows.
    # The manifest represents document content rather than checkout-specific
    # line endings, so verify the canonical LF byte sequence on every host.
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def fetch(url: str, logger: logging.Logger, attempts: int = 8) -> tuple[bytes, dict[str, str]]:
    global _next_request_at
    if not url.startswith("https://docs.alpaca.markets/"):
        raise ValueError(f"拒绝非 Alpaca 官方地址: {url}")
    for attempt in range(1, attempts + 1):
        with _rate_lock:
            delay = max(0.0, _next_request_at - time.monotonic())
            if delay:
                time.sleep(delay)
            _next_request_at = time.monotonic() + _minimum_interval
        started = time.monotonic()
        try:
            with tempfile.TemporaryDirectory(prefix="alpaca-doc-fetch-") as temp_dir:
                body_path = Path(temp_dir) / "body"
                header_path = Path(temp_dir) / "headers"
                command = [
                        "curl", "--fail", "--silent", "--show-error", "--location",
                        "--max-time", "45", "--connect-timeout", "10", "--http1.1",
                        "--proto", "=https", "--proto-redir", "=https", "--max-redirs", "2",
                        "--max-filesize", "33554432",
                        "--user-agent", "Alpaca_Docs/1.0",
                        "--header", "Accept-Encoding: identity",
                        "--dump-header", str(header_path), "--output", str(body_path),
                ]
                resolve_ip = os.getenv("ALPACA_DOCS_RESOLVE_IP", "")
                if resolve_ip:
                    ipaddress.ip_address(resolve_ip)
                    command.extend(["--resolve", f"docs.alpaca.markets:443:{resolve_ip}"])
                command.append(url)
                subprocess.run(
                    command,
                    check=True,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.PIPE,
                    text=True,
                )
                body = body_path.read_bytes()
                if not body:
                    raise RuntimeError("响应正文为空")
                header_blocks = header_path.read_text(encoding="iso-8859-1").strip().split("\r\n\r\n")
                headers: dict[str, str] = {}
                for line in header_blocks[-1].splitlines()[1:]:
                    if ":" in line:
                        key, value = line.split(":", 1)
                        headers[key.strip().lower()] = value.strip()
                logger.debug(
                    "下载成功 url=%s 尝试=%d 字节=%d 耗时毫秒=%.2f",
                    url, attempt, len(body), (time.monotonic() - started) * 1000,
                )
                return body, headers
        except (OSError, RuntimeError, subprocess.CalledProcessError) as exc:
            logger.warning("下载失败 url=%s 尝试=%d/%d 错误类型=%s 错误=%s", url, attempt, attempts, type(exc).__name__, exc)
            if attempt == attempts:
                raise
            # 官方 CDN 在批量同步时可能返回 429。较长的有界退避可保护官方服务，
            # 也让每周无人值守任务有机会在限流窗口结束后自行恢复。
            time.sleep(min(60.0, 5.0 * (2 ** (attempt - 1))))
    raise AssertionError("不可达")


def local_page_path(root: Path, url: str) -> Path:
    relative = url.removeprefix("https://docs.alpaca.markets/us/")
    if relative.startswith("/") or ".." in Path(relative).parts:
        raise ValueError(f"非法文档路径: {url}")
    return root / "pages" / relative


def page_urls(index_text: str) -> list[str]:
    """从官方 llms.txt 动态提取全部 US 文档和 API Reference 页面 URL。"""
    return sorted(set(LINK_RE.findall(index_text)))


def manifest_entry(url: str, path: Path, body: bytes, headers: dict[str, str], root: Path) -> dict[str, Any]:
    return {
        "source_url": url,
        "retrieved_at": datetime.now(UTC).isoformat(),
        "etag": headers.get("etag", ""),
        "last_modified": headers.get("last-modified", ""),
        "sha256": sha256(body),
        "bytes": len(body),
        "local_path": path.relative_to(root).as_posix(),
        "status": "updated",
    }


def individual_page_errors(root: Path, entries: list[dict[str, Any]]) -> list[str]:
    """确认每个官方页面 URL 都映射为一个独立且唯一的本地文件。"""
    errors: list[str] = []
    source_urls: set[str] = set()
    local_paths: set[str] = set()
    for entry in entries:
        local_path = entry["local_path"]
        if not local_path.startswith("pages/"):
            continue
        source_url = entry["source_url"]
        expected_path = local_page_path(root, source_url).relative_to(root).as_posix()
        if local_path != expected_path:
            errors.append(
                f"官方页面未保持独立路径: 来源={source_url} "
                f"期望={expected_path} 实际={local_path}"
            )
        if source_url in source_urls:
            errors.append(f"官方页面 URL 重复映射: {source_url}")
        if local_path in local_paths:
            errors.append(f"本地页面路径重复映射: {local_path}")
        source_urls.add(source_url)
        local_paths.add(local_path)
    return errors


def page_title(body: bytes, fallback: str) -> str:
    """提取 Markdown 一级标题，用于稳定的离线 API Reference 索引。"""
    for line in body.decode("utf-8").splitlines():
        if line.startswith("# "):
            return line.removeprefix("# ").strip()
    return fallback


def write_reference_index(root: Path, entries: list[dict[str, Any]]) -> None:
    """生成由受管页面清单驱动的本地 API Reference 导航页。"""
    references = sorted(
        (entry for entry in entries if entry["local_path"].startswith("pages/reference/")),
        key=lambda entry: entry["local_path"],
    )
    lines = [
        "# Alpaca API Reference 本地索引",
        "",
        "本文件由 `scripts/sync_alpaca_docs.py` 生成；请勿手工修改。",
        "它只提供导航，**不包含或合并任何页面正文**。",
        "每个官方 URL 都独立保存在与其 URL 路径对应的 `pages/reference/*.md` 文件中。",
        "完整 OpenAPI 契约位于 `openapi/`，页面正文和嵌入的接口说明位于 `pages/reference/`。",
        "",
        f"- Reference 页面数：{len(references)}",
        "- 快速全文查询：`rg -n -i '关键词' docs/pages docs/openapi`",
        "",
        "| API Reference | 本地文件 | 官方来源 |",
        "| --- | --- | --- |",
    ]
    for entry in references:
        path = root / entry["local_path"]
        title = page_title(path.read_bytes(), Path(entry["local_path"]).stem)
        local_path = entry["local_path"]
        lines.append(
            f"| {title} | [`{local_path}`]({local_path}) | "
            f"[官方页面]({entry['source_url']}) |"
        )
    atomic_write_bytes(root / "api-reference-index.md", ("\n".join(lines) + "\n").encode("utf-8"))


def sync(root: Path, scope: str, workers: int, logger: logging.Logger) -> None:
    logger.info("开始同步 scope=%s 输出目录=%s 并发数=%d", scope, root, workers)
    previous_entries: dict[str, dict[str, Any]] = {}
    previous_manifest: dict[str, Any] | None = None
    previous_manifest_path = root / "manifest.json"
    if previous_manifest_path.is_file():
        previous_manifest = json.loads(previous_manifest_path.read_text(encoding="utf-8"))
        previous_entries = {entry["local_path"]: entry for entry in previous_manifest.get("entries", [])}
    index_body, index_headers = fetch(INDEX_URL, logger)
    index_text = index_body.decode("utf-8")
    urls = page_urls(index_text)
    if scope == "relevant":
        urls = [url for url in urls if any(token in url.lower() for token in RELEVANT)]
    if not urls:
        raise RuntimeError("Alpaca llms.txt 未发现任何 /us/docs/ 或 /us/reference/ Markdown 页面")
    if previous_manifest is not None:
        previous_count = int(previous_manifest.get("document_count", 0) or 0)
        if previous_count >= 20 and len(urls) < previous_count * 0.8:
            raise RuntimeError(
                f"官方索引页面数异常下降: 原={previous_count} 现={len(urls)}；"
                "为避免无人值守任务大量删除缓存，本次同步失败并等待人工复核"
            )
    logger.info("文档索引解析完成 候选文档数=%d 索引字节=%d", len(urls), len(index_body))
    index_path = root / "llms.txt"
    atomic_write_bytes(index_path, index_body)
    entries: list[dict[str, Any]] = [manifest_entry(INDEX_URL, index_path, index_body, index_headers, root)]

    def download_page(url: str) -> dict[str, Any]:
        body, headers = fetch(url, logger)
        path = local_page_path(root, url)
        atomic_write_bytes(path, body)
        return manifest_entry(url, path, body, headers, root)

    failures: list[tuple[str, str]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(download_page, url): url for url in urls}
        completed = 0
        for future in concurrent.futures.as_completed(futures):
            url = futures[future]
            try:
                entries.append(future.result())
            except Exception as exc:  # noqa: BLE001 - 汇总所有下载错误后整体失败
                failures.append((url, f"{type(exc).__name__}: {exc}"))
                logger.error("文档同步失败 url=%s 错误=%s", url, failures[-1][1])
            completed += 1
            if completed % 100 == 0 or completed == len(urls):
                logger.info("文档同步进度 已完成=%d 总数=%d 失败=%d", completed, len(urls), len(failures))

    for filename, url in SPEC_URLS.items():
        body, headers = fetch(url, logger)
        parsed = json.loads(body)
        if not isinstance(parsed, dict) or "openapi" not in parsed or "paths" not in parsed:
            raise RuntimeError(f"OpenAPI 结构无效: {url}")
        path = root / "openapi" / filename
        atomic_write_bytes(path, json.dumps(parsed, ensure_ascii=False, indent=2, sort_keys=True).encode("utf-8") + b"\n")
        normalized = path.read_bytes()
        entries.append(manifest_entry(url, path, normalized, headers, root))
        logger.info("OpenAPI 同步完成 文件=%s 接口路径数=%d 字节=%d", filename, len(parsed["paths"]), len(normalized))

    current_paths = {entry["local_path"] for entry in entries}
    removed_paths = set(previous_entries) - current_paths
    content_changed = bool(removed_paths) or set(previous_entries) != current_paths
    for entry in entries:
        previous = previous_entries.get(entry["local_path"])
        if previous is None:
            entry["status"] = "added"
        elif previous.get("sha256") == entry["sha256"]:
            # 内容未变时保留原始检索元数据，确保定时检查不会制造空变更 PR。
            entry.update(previous)
        else:
            entry["status"] = "updated"
            content_changed = True
    generated_at = datetime.now(UTC).isoformat()
    if not content_changed and previous_manifest_path.is_file():
        generated_at = previous_manifest.get("generated_at", generated_at)
    manifest = {
        "schema_version": 1,
        "scope": scope,
        "generated_at": generated_at,
        "source_index": INDEX_URL,
        "document_count": len(urls),
        "entries": sorted(entries, key=lambda item: item["local_path"]),
        "failures": [{"source_url": url, "error": error} for url, error in failures],
    }
    if not failures:
        mapping_errors = individual_page_errors(root, entries)
        if mapping_errors:
            raise RuntimeError("；".join(mapping_errors))
        for stale_path in sorted(removed_paths):
            candidate = (root / stale_path).resolve()
            if root.resolve() not in candidate.parents or not candidate.is_file():
                raise RuntimeError(f"拒绝删除清单范围外文件: {stale_path}")
            candidate.unlink()
            logger.info("删除官方索引已移除的本地受管文件 路径=%s", stale_path)
        write_reference_index(root, entries)
    atomic_write_bytes(root / "manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True).encode("utf-8") + b"\n")
    if failures:
        raise RuntimeError(f"存在 {len(failures)} 个下载失败，详见 manifest.json")
    logger.info("全部同步完成 文档数=%d OpenAPI数=%d 清单条目数=%d", len(urls), len(SPEC_URLS), len(entries))


def verify(root: Path, logger: logging.Logger) -> None:
    manifest_path = root / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors: list[str] = []
    if manifest.get("failures"):
        errors.append(f"清单仍包含下载失败: {len(manifest['failures'])}")
    expected_entries = int(manifest.get("document_count", -1)) + len(SPEC_URLS) + 1
    if len(manifest.get("entries", [])) != expected_entries:
        errors.append(f"清单条目数异常: 期望={expected_entries} 实际={len(manifest.get('entries', []))}")
    for entry in manifest["entries"]:
        path = root / entry["local_path"]
        if not path.is_file():
            errors.append(f"文件缺失: {entry['local_path']}")
            continue
        actual = sha256(path.read_bytes())
        if actual != entry["sha256"]:
            errors.append(f"哈希不匹配: {entry['local_path']}")
    errors.extend(individual_page_errors(root, manifest["entries"]))
    for spec in SPEC_URLS:
        parsed = json.loads((root / "openapi" / spec).read_text(encoding="utf-8"))
        if "openapi" not in parsed or "paths" not in parsed:
            errors.append(f"OpenAPI 结构无效: {spec}")
    reference_entries = [
        entry for entry in manifest["entries"]
        if entry["local_path"].startswith("pages/reference/")
    ]
    reference_index = root / "api-reference-index.md"
    if not reference_index.is_file():
        errors.append("API Reference 本地索引缺失: api-reference-index.md")
    else:
        index_text = reference_index.read_text(encoding="utf-8")
        for entry in reference_entries:
            if entry["local_path"] not in index_text:
                errors.append(f"API Reference 索引缺少页面: {entry['local_path']}")
    if errors:
        for error in errors:
            logger.error("校验失败 原因=%s", error)
        raise RuntimeError(f"本地文档校验失败，错误数={len(errors)}")
    logger.info("本地文档校验通过 清单条目数=%d", len(manifest["entries"]))



def transactional_sync(root: Path, scope: str, workers: int, logger: logging.Logger) -> None:
    """Build and verify a staging mirror before atomically replacing the live directory."""
    root = root.resolve()
    root.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".{root.name}.staging-", dir=root.parent)).resolve()
    backup: Path | None = None
    try:
        if root.is_dir():
            shutil.copytree(root, staging, dirs_exist_ok=True)
        elif root.exists():
            raise RuntimeError(f"输出路径不是目录: {root}")

        sync(staging, scope, workers, logger)
        verify(staging, logger)

        if root.exists():
            backup = root.with_name(f".{root.name}.backup-{uuid.uuid4().hex}")
            os.replace(root, backup)
        try:
            os.replace(staging, root)
        except BaseException:
            if backup is not None and backup.exists() and not root.exists():
                os.replace(backup, root)
            raise

        if backup is not None and backup.exists():
            shutil.rmtree(backup)
            backup = None
    finally:
        if staging.exists():
            shutil.rmtree(staging)
        if backup is not None and backup.exists() and root.exists():
            shutil.rmtree(backup)


def main(argv: list[str] | None = None) -> int:
    global _minimum_interval
    parser = argparse.ArgumentParser(description="同步或校验 Alpaca 官方文档")
    parser.add_argument("command", choices=("sync", "verify"))
    parser.add_argument("--scope", choices=("relevant", "all-us"), default="all-us")
    parser.add_argument("--output", type=Path, default=Path("docs"))
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--min-interval", type=float, default=0.35, help="官方请求之间的最小秒数")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args(argv)
    if args.workers <= 0 or args.min_interval < 0:
        parser.error("workers 必须大于零，min-interval 不能为负数")
    _minimum_interval = args.min_interval
    logger = configure_logging(args.debug or os.getenv("LOG_LEVEL", "").upper() == "DEBUG")
    try:
        if args.command == "sync":
            transactional_sync(args.output, args.scope, args.workers, logger)
        else:
            verify(args.output, logger)
    except Exception as exc:  # noqa: BLE001 - 顶层统一输出中文诊断
        logger.exception("命令执行失败 命令=%s 错误类型=%s 错误=%s", args.command, type(exc).__name__, exc)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
