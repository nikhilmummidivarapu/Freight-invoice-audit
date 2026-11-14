from sqlalchemy import Column, Integer, DateTime, Numeric, ForeignKey
from app.database.base import Base
class WeightMeasurement(Base):
    __tablename__ = "weight_measurements"
    id = Column(Integer, primary_key=True, autoincrement=True)
    shipment_id = Column(Integer, ForeignKey("shipments.id"), nullable=False)
    actual_weight_kg = Column(Numeric(12,2))
    dimensional_weight_kg = Column(Numeric(12,2))
    chargeable_weight_kg = Column(Numeric(12,2))
    measured_at = Column(DateTime)
