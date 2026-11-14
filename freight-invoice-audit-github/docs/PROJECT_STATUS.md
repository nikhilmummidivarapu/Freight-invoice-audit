# Project status and handover

## Completed
- MySQL `freight_audit` database and 11 core tables.
- Added `billed_shipment_reference` to `freight_invoices`.
- Local baseline counts: 100 carriers, 10 lanes, 100 rate cards, 500 shipments, 500 shipment legs, 500 weight measurements, 198 accessorials, 500 invoices, 1,641 invoice lines.
- Seven checks: shipment reference, rate card validity, weight, accessorials, fuel, tax (18%), invoice total.
- Clean baseline passed 3,500/3,500 checks.
- `ground_truth` table created.
- First anomaly injected: `FINV-2026-000001`, reference `SHP-2026-000001` changed to `SHP-2026-999999`.
- Combined audit detected 1 failed shipment-reference check; other 2,999 checks passed.

## Current stopping point
First anomaly successfully detected and recorded in `ground_truth`. Next: inspect rate-card and shipment rows for a carefully chosen invoice, then implement anomaly 2 (expired rate card) in a reversible way.

## Remaining anomaly scenarios
1. Expired rate card.
2. Wrong weight-based charge.
3. Duplicate fuel surcharge / duplicate invoice line.
4. Over-credit (requires an exception and credit-note validation rule).

## Known limitations
- Current combined audit prints failures but does not insert into `audit_exceptions`.
- Rate-card join assumes one card per carrier/lane and is an inner join. Improve to handle missing, overlapping and multiple valid cards.
- Duplicate invoice-line and credit-note checks are not implemented yet.
- Original data generator scripts are not reconstructed in this package; copy them from the original local project if available. They were not idempotent, so do not rerun on populated data.
- The ORM definitions are a repository reconstruction from the project schema notes. Compare them with the original local models before applying schema changes to an existing database.
