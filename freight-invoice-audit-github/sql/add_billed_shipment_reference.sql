USE freight_audit;
-- Run only if this column does not already exist.
ALTER TABLE freight_invoices
ADD COLUMN billed_shipment_reference VARCHAR(40) NULL;
