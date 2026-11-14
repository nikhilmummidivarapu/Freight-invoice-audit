
import sys
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import text
from app.database.connection import engine

query = '''
SELECT
    i.invoice_code,
    i.billed_shipment_reference,
    i.base_amount,
    i.fuel_surcharge,
    i.accessorial_amount,
    i.tax_amount,
    i.total_amount,
    s.shipment_code,
    s.shipment_date,
    s.actual_weight_kg,
    s.length_cm,
    s.width_cm,
    s.height_cm,
    w.dimensional_weight_kg,
    w.chargeable_weight_kg,
    r.effective_from,
    r.effective_to,
    r.status,
    r.base_rate,
    r.rate_per_kg,
    r.fuel_surcharge_percent,
    COALESCE(a.expected_amount, 0) AS expected_accessorial
FROM freight_invoices i
JOIN shipments s ON i.shipment_id = s.id
JOIN weight_measurements w ON s.id = w.shipment_id
JOIN rate_cards r
    ON r.carrier_id = i.carrier_id
    AND r.lane_id = s.lane_id
LEFT JOIN (
    SELECT shipment_id, SUM(amount) AS expected_amount
    FROM accessorials
    WHERE status = 'APPROVED'
    GROUP BY shipment_id
) a ON a.shipment_id = s.id
'''

with engine.connect() as connection:
    records = connection.execute(text(query)).fetchall()

rules = {
    name: [0, 0] for name in [
        "Shipment Reference",
        "Rate Card",
        "Shipment Weight",
        "Freight Charge Calculation",
        "Accessorial Charges",
        "Fuel Surcharge",
        "Tax Calculation",
        "Invoice Total"
    ]
}


def check(name, valid, invoice):
    rules[name][0 if valid else 1] += 1

    if not valid:
        print("FAILED:", name, "-", invoice)


for r in records:

    actual = Decimal(str(r.actual_weight_kg))

    dimensional = (
        Decimal(str(r.length_cm)) *
        Decimal(str(r.width_cm)) *
        Decimal(str(r.height_cm)) /
        Decimal("5000")
    ).quantize(Decimal("0.01"))

    chargeable = max(actual, dimensional).quantize(Decimal("0.01"))

    base, fuel, accessorial, tax, total = map(
        Decimal,
        map(str, [
            r.base_amount,
            r.fuel_surcharge,
            r.accessorial_amount,
            r.tax_amount,
            r.total_amount
        ])
    )

    expected_base = (
        Decimal(str(r.base_rate)) +
        chargeable * Decimal(str(r.rate_per_kg))
    ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    expected_fuel = (
        base * Decimal(str(r.fuel_surcharge_percent)) /
        Decimal("100")
    ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    expected_accessorial = Decimal(str(r.expected_accessorial))

    expected_tax = (
        (base + fuel + accessorial) * Decimal("0.18")
    ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    check(
        "Shipment Reference",
        r.billed_shipment_reference == r.shipment_code,
        r.invoice_code
    )

    check(
        "Rate Card",
        r.effective_from <= r.shipment_date <= r.effective_to
        and r.status == "ACTIVE",
        r.invoice_code
    )

    check(
        "Shipment Weight",
        Decimal(str(r.dimensional_weight_kg)) == dimensional
        and Decimal(str(r.chargeable_weight_kg)) == chargeable,
        r.invoice_code
    )

    check(
        "Freight Charge Calculation",
        base == expected_base,
        r.invoice_code
    )

    check(
        "Accessorial Charges",
        accessorial == expected_accessorial,
        r.invoice_code
    )

    check(
        "Fuel Surcharge",
        fuel == expected_fuel,
        r.invoice_code
    )

    check(
        "Tax Calculation",
        tax == expected_tax,
        r.invoice_code
    )

    check(
        "Invoice Total",
        total == base + fuel + accessorial + tax,
        r.invoice_code
    )


print("\nFREIGHT INVOICE AUDIT REPORT")
print("=" * 40)

passed = failed = 0

for name, (p, f) in rules.items():
    passed += p
    failed += f
    print(f"{name}: Passed {p}, Failed {f}")

print("-" * 40)
print("Total checks:", passed + failed)
print("Passed:", passed)
print("Failed:", failed)
