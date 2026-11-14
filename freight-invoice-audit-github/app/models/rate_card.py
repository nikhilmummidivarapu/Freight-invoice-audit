from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from app.database.base import Base
class RateCard(Base):
    __tablename__ = "rate_cards"
    id = Column(Integer, primary_key=True, autoincrement=True)
    rate_card_code = Column(String(50), unique=True, nullable=False)
    carrier_id = Column(Integer, ForeignKey("carriers.id"), nullable=False)
    lane_id = Column(Integer, ForeignKey("lanes.id"), nullable=False)
    base_rate = Column(Numeric(12,2))
    rate_per_kg = Column(Numeric(12,2))
    fuel_surcharge_percent = Column(Numeric(6,2))
    effective_from = Column(Date)
    effective_to = Column(Date)
    status = Column(String(30))
