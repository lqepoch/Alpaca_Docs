"""Offline regression tests for the standalone Alpaca documentation synchronizer."""

from __future__ import annotations

import importlib.util
import json
import logging
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "sync_alpaca_docs.py"
SPEC = importlib.util.spec_from_file_location("sync_alpaca_docs", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
sync = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sync)

class SyncTests(unittest.TestCase):
    def test_hash_is_stable_across_windows_line_endings(self) -> None:
        self.assertEqual(sync.sha256(b"first\nsecond\n"), sync.sha256(b"first\r\nsecond\r\n"))

    def test_page_urls_are_unique_and_sorted(self) -> None:
        text = """
        [B](https://docs.alpaca.markets/us/reference/z-page.md)
        [A](https://docs.alpaca.markets/us/docs/a-page.md)
        [B2](https://docs.alpaca.markets/us/reference/z-page.md)
        """
        self.assertEqual(sync.page_urls(text), [
            "https://docs.alpaca.markets/us/docs/a-page.md",
            "https://docs.alpaca.markets/us/reference/z-page.md",
        ])

    def test_official_page_maps_to_its_own_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            url = "https://docs.alpaca.markets/us/reference/getaccount-1.md"
            path = sync.local_page_path(root, url)
            self.assertEqual(path.relative_to(root).as_posix(), "pages/reference/getaccount-1.md")

    def test_off_domain_input_is_rejected(self) -> None:
        logger = logging.getLogger("test")
        with self.assertRaises(ValueError):
            sync.fetch("https://example.com/a.md", logger, attempts=1)

    def test_reference_index_is_sorted(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first = root / "pages/reference/a.md"
            second = root / "pages/reference/z.md"
            first.parent.mkdir(parents=True)
            first.write_text("# A endpoint\n", encoding="utf-8")
            second.write_text("# Z endpoint\n", encoding="utf-8")
            entries = [
                {"local_path": "pages/reference/z.md", "source_url": "https://docs.alpaca.markets/us/reference/z.md"},
                {"local_path": "pages/reference/a.md", "source_url": "https://docs.alpaca.markets/us/reference/a.md"},
            ]
            sync.write_reference_index(root, entries)
            index = (root / "api-reference-index.md").read_text(encoding="utf-8")
            self.assertLess(index.index("pages/reference/a.md"), index.index("pages/reference/z.md"))

    def test_atomic_write_replaces_content(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nested" / "value.txt"
            sync.atomic_write_bytes(path, b"one\n")
            sync.atomic_write_bytes(path, b"two\n")
            self.assertEqual(path.read_bytes(), b"two\n")


if __name__ == "__main__":
    unittest.main()
