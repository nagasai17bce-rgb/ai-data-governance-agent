# AI Data Governance Agent

A policy-oriented API that classifies sensitive-looking fields and requires approval before restrictive actions.

## Run
```bash
pip install -e '.[dev]'
uvicorn app.main:app --reload
```

Send comma-separated field names to `/v1/run`.

## Production extensions
Integrate a metadata catalog, policy-as-code, PII classifiers, lineage, masking/tokenization providers, audit logs, and approval workflows.
