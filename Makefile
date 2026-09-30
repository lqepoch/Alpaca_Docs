.PHONY: test sync verify

test:
	PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -p 'test_*.py' -v

sync:
	PYTHONDONTWRITEBYTECODE=1 python scripts/sync_alpaca_docs.py sync --output docs --scope all-us --workers 3

verify:
	PYTHONDONTWRITEBYTECODE=1 python scripts/sync_alpaca_docs.py verify --output docs
