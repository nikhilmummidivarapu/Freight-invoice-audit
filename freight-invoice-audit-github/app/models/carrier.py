from sqlalchemy import Column, Integer, String, DateTime
from app.database.base import Base
class Carrier(Base):
    __tablename__ = "carriers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    carrier_code = Column(String(30), unique=True, nullable=False)
    carrier_name = Column(String(150), nullable=False)
    contact_email = Column(String(150))
    phone = Column(String(30))
    status = Column(String(30))
    created_at = Column(DateTime)
