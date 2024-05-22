from sqlalchemy import Column, Integer, String, Float
from database import Base

# Define the location model
class Location(Base):
    __tablename__ = "locations"
    location_id = Column(Integer, primary_key=True, index=True)
    location_name = Column(String, index=True)
    lat = Column(Float)
    lon = Column(Float)
    radius = Column(Float)

# Define the device model
class Device(Base):
    __tablename__ = "devices"
    device_id = Column(Integer, primary_key=True, index=True)
    device_name = Column(String, index=True)
    lat = Column(Float)
    lon = Column(Float)
