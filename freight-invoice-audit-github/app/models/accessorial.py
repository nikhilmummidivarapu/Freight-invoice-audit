from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from app.database.base import Base
class Accessorial(Base):
    __tablename__ = "accessorials"
    id = Column(Integer, primary_key=True, autoincrement=True)
    shipment_id = Column(Integer, ForeignKey("shipments.id"), nullable=False)
    charge_code = Column(String(40))
    description = Column(String(255))
    amount = Column(Numeric(12,2))
    status = Column(String(30))
    charge_date = Column(Date)
