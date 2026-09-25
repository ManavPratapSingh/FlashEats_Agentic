# Architecture

This is intentionally a small application.

```text
Browser
  ↓
Flask API
  ↓
Service layer
  ↓
JSON source data
```

## Boundaries

- `backend/api.py` owns HTTP routes.
- `backend/services/orders.py` owns order retrieval.
- `backend/services/risk.py` owns the existing risk business rule.
- `frontend/` should consume backend APIs rather than reading `backend/data/orders.json` directly.
- tests encode behavior that existing consumers may rely on.

## Change preference

Prefer the smallest change that fits the current architecture.

Do not introduce a database, frontend framework, queue, or new service unless the feature genuinely requires it.
