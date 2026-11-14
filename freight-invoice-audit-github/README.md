# Freight Invoice Audit & Validation System

Python + MySQL project for validating freight invoices against shipment references, rate cards, weights, approved accessorials, fuel surcharge, tax and invoice totals.

## Current status
- MySQL database: `freight_audit`
- Baseline in the user's local database: 100 carriers, 10 lanes, 100 rate cards, 500 shipments, 500 shipment legs, 500 weight measurements, 198 accessorials, 500 invoices and 1,641 invoice lines.
- Seven audit rules implemented.
- Clean baseline: 3,500 checks passed, 0 failed.
- First anomaly injected and detected: invoice `FINV-2026-000001`, billed reference changed from `SHP-2026-000001` to `SHP-2026-999999`.
- Four planned anomalies remain: expired rate card, wrong weight charge, duplicate surcharge, and over-credit.

## Stack
Python 3.12, MySQL 8, SQLAlchemy, PyMySQL, python-dotenv, Pandas, Faker, FastAPI, Streamlit, Pydantic, Pytest.

## Setup (Windows CMD)
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```
Create database `freight_audit`, copy `.env.example` to `.env`, and enter your own local database password. Never commit `.env`.

```cmd
python scripts\test_db.py
python scripts\create_tables.py
python scripts\run_audit.py
```

## Important
The original synthetic-data generator scripts were run in the user's existing project, but their exact source code was not available during this repository reconstruction. Copy those generator scripts from the original local project if available. The original generators were not idempotent: do not rerun them against an already populated database.

`Base.metadata.create_all()` creates missing tables but does not modify existing tables. Use the SQL migration in `sql/` only if the column is not already present.

The current combined audit is a prototype:
- It prints failures but does not yet save them into `audit_exceptions`.
- Its rate-card join assumes one matching card per carrier/lane.
- Its inner join can omit invoices without a matching rate card.
- Duplicate invoice-line and credit-note checks are not yet implemented.

See `docs/PROJECT_STATUS.md` and `docs/GITHUB_UPLOAD_GUIDE.md`.
