from sqlalchemy import Column, Integer, String, Date, DateTime, Numeric, ForeignKey
from app.database.base import Base
class FreightInvoice(Base):
    __tablename__ = "freight_invoices"
    id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_code = Column(String(50), unique=True, nullable=False)
    carrier_id = Column(Integer, ForeignKey("carriers.id"), nullable=False)
    shipment_id = Column(Integer, ForeignKey("shipments.id"), nullable=False)
    billed_shipment_reference = Column(String(40), nullable=True)
    invoice_date = Column(Date)
    due_date = Column(Date)
    base_amount = Column(Numeric(12,2))
    fuel_surcharge = Column(Numeric(12,2))
    accessorial_amount = Column(Numeric(12,2))
    tax_amount = Column(Numeric(12,2))
    total_amount = Column(Numeric(12,2))
    currency = Column(String(10))
    status = Column(String(30))
    created_at = Column(DateTime)
