from sqlalchemy import Column, Integer, String, Float, BigInteger
from db.base import Base


class MeterReading(Base):
    __tablename__="meter_readings"

    id = Column(Integer, primary_key=True, index=True)
    meter_id = Column(String, index=True)
    usage_kwh = Column(Float)
    cost = Column(Float)
    timestamp = Column(BigInteger)
