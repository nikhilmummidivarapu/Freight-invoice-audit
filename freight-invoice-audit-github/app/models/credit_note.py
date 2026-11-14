from sqlalchemy import Column, Integer, String, Date, DateTime, Numeric, ForeignKey
from app.database.base import Base
class CreditNote(Base):
    __tablename__ = "credit_notes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    credit_note_code = Column(String(50), unique=True, nullable=False)
    invoice_id = Column(Integer, ForeignKey("freight_invoices.id"), nullable=False)
    exception_id = Column(Integer, ForeignKey("audit_exceptions.id"), nullable=True)
    credit_date = Column(Date)
    credit_amount = Column(Numeric(12,2))
    reason = Column(String(500))
    status = Column(String(30))
    created_at = Column(DateTime)
