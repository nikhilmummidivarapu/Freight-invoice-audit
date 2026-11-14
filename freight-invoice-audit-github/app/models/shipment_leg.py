from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database.base import Base
class ShipmentLeg(Base):
    __tablename__ = "shipment_legs"
    id = Column(Integer, primary_key=True, autoincrement=True)
    shipment_id = Column(Integer, ForeignKey("shipments.id"), nullable=False)
    leg_number = Column(Integer)
    origin = Column(String(150))
    destination = Column(String(150))
    departure_date = Column(Date)
    arrival_date = Column(Date)
    status = Column(String(30))
