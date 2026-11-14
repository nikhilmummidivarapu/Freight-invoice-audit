from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from app.database.base import Base
class InvoiceLine(Base):
    __tablename__ = "invoice_lines"
    id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_id = Column(Integer, ForeignKey("freight_invoices.id"), nullable=False)
    line_code = Column(String(60), unique=True, nullable=False)
    charge_type = Column(String(40))
    description = Column(String(255))
    quantity = Column(Numeric(12,2))
    unit_rate = Column(Numeric(12,2))
    amount = Column(Numeric(12,2))
