from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey
from app.database.base import Base
class AuditException(Base):
    __tablename__ = "audit_exceptions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    exception_code = Column(String(50), unique=True, nullable=False)
    invoice_id = Column(Integer, ForeignKey("freight_invoices.id"), nullable=False)
    invoice_line_id = Column(Integer, ForeignKey("invoice_lines.id"), nullable=True)
    exception_type = Column(String(100))
    description = Column(String(500))
    expected_amount = Column(Numeric(12,2))
    actual_amount = Column(Numeric(12,2))
    difference_amount = Column(Numeric(12,2))
    severity = Column(String(30))
    status = Column(String(30))
    detected_at = Column(DateTime)
