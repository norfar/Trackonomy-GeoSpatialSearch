from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
import math
import models
import database
import init_db

# Initialize FastAPI app
app = FastAPI()

# Base model for search response
class SearchBase(BaseModel):
    location_id: int
    found_devices: list[str]

# Base model for location data
class LocationBase(BaseModel):
    location_id: int
    location_name: str
    lat: float
    lon: float
    radius: float

# Base model for device data
class DeviceBase(BaseModel):
    device_id: int 
    device_name: str
    lat: float
    lon: float

# Dependency function to get a database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Event handler to initialize database on app startup
def startup_event():
    db = database.SessionLocal()
    try:
        init_db.init_data(db)
    finally:
        db.close()

# Attach startup event handler to the app
app.add_event_handler("startup", startup_event)

# Endpoint to get all locations
@app.get("/locations", response_model=list[LocationBase])
def get_devices(db: Session = Depends(get_db)):
    devices = db.query(models.Location).all()
    return devices

# Endpoint to get all devices
@app.get("/devices", response_model=list[DeviceBase])
def get_devices(db: Session = Depends(get_db)):
    devices = db.query(models.Device).all()
    return devices

# Function to calculate haversine distance between two points
def haversine(lat1, lon1, lat2, lon2):
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    # Radius of earth in miles is 3963
    distance = 3963.1906 * c
    return round(distance, 4)

# Endpoint to find devices within the radius of a location
@app.get("/search/{location_id}", response_model=SearchBase)
def get_devices_within_radius(location_id: int, db: Session = Depends(get_db)):
    # Retrieve location from the database
    location = db.query(models.Location).filter(models.Location.location_id == location_id).first()
    
    # If location not found, raise HTTPException
    if location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    
    # List to store devices found within the radius
    devices_in_radius = []
    # Query all devices
    devices = db.query(models.Device).all()
    
    # Iterate through devices to check if they're within the radius of the given location
    for device in devices:
        distance = haversine(location.lat, location.lon, device.lat, device.lon)
        if distance <= location.radius:
            devices_in_radius.append(device.device_name)
    
    # Return response containing location ID and found devices
    return {"location_id": location_id, "found_devices": devices_in_radius}
