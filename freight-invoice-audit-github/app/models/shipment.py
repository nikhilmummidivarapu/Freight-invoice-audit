from sqlalchemy import Column, Integer, String, Date, DateTime, Numeric, ForeignKey
from app.database.base import Base
class Shipment(Base):
    __tablename__ = "shipments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    shipment_code = Column(String(40), unique=True, nullable=False)
    carrier_id = Column(Integer, ForeignKey("carriers.id"), nullable=False)
    lane_id = Column(Integer, ForeignKey("lanes.id"), nullable=False)
    shipment_date = Column(Date)
    delivery_date = Column(Date)
    actual_weight_kg = Column(Numeric(12,2))
    length_cm = Column(Numeric(10,2))
    width_cm = Column(Numeric(10,2))
    height_cm = Column(Numeric(10,2))
    status = Column(String(30))
    created_at = Column(DateTime)
