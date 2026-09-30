# Alpaca_Docs

Public, automatically refreshed local cache of Alpaca official US documentation and OpenAPI specifications.

## Repository layout

- docs/llms.txt — official Alpaca US documentation index.
- docs/pages/docs/ — one Markdown file per official US guide page.
- docs/pages/reference/ — one Markdown file per official API Reference page.
- docs/openapi/ — Trading API, Market Data API, and Broker API OpenAPI JSON.
- docs/api-reference-index.md — generated local API Reference navigation.
- docs/manifest.json — source URL, retrieval metadata, SHA-256, byte count, local path, and change status.
- scripts/sync_alpaca_docs.py — credential-free standalone synchronizer.

## Automation

GitHub Actions runs every Sunday at 08:17 China Standard Time / Singapore Time (00:17 UTC), and can also be started manually. Changes to the synchronizer, tests, workflow, Makefile, or line-ending policy trigger a validation run on main.

Each run executes offline tests, downloads the current public llms.txt index, mirrors every discovered /us/docs/ and /us/reference/ Markdown page, downloads the three official OpenAPI specifications, verifies all hashes and path mappings, then commits only verified docs changes.

The sync is staged in a temporary directory and replaces docs only after verification passes. If the indexed page count suddenly falls by more than 20 percent, the unattended run fails closed so a transient upstream/index failure cannot delete a large part of the cache.

## Local commands

make test
make sync
make verify

Search locally with: rg -n -i 'option|websocket|rate limit' docs/pages docs/openapi

## Security and provenance

The synchronizer reads only public HTTPS resources under docs.alpaca.markets. It does not require or read Alpaca trading credentials, broker credentials, cookies, database DSNs, or account data. Downloads are rate-limited, retried with bounded backoff, HTTPS-only, redirect-limited, and capped at 32 MiB per response.

The official Alpaca documentation remains authoritative. This repository is a cache and can lag upstream between scheduled runs.

## Licensing

The repository LICENSE applies to the synchronization software in this repository. Mirrored Alpaca documentation and API specifications remain third-party material subject to Alpaca applicable rights and terms; the repository license does not relicense that content.
