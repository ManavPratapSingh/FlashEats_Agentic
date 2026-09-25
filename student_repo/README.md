# FlashEats Operations Console

FlashEats Operations uses this small internal application to inspect active food-delivery orders.

## Current capability

The application currently supports:

- listing orders,
- viewing an individual order,
- calculating whether an order is considered at risk,
- a basic browser UI for viewing orders.

The Operations team has now asked for a way to surface **delayed / risky orders** so they can focus attention where intervention may be needed.

> Do not assume the wording in this README is the complete business specification. Inspect the repository and product documentation before changing code.

## Run locally

```bash
python -m pip install -r requirements.txt
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Run tests

```bash
pytest -q
```

## Engineering expectation

Before implementing a feature:

1. inspect the repository,
2. identify existing business rules and API contracts,
3. identify ambiguities,
4. propose a minimal plan,
5. make small verifiable changes,
6. run and review tests.
