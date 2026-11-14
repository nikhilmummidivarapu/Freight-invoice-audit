from sqlalchemy import Column, Integer, String, Float
from app.database.base import Base
class Lane(Base):
    __tablename__ = "lanes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    lane_code = Column(String(30), unique=True, nullable=False)
    origin_city = Column(String(100))
    origin_state = Column(String(100))
    destination_city = Column(String(100))
    destination_state = Column(String(100))
    distance_km = Column(Float)
