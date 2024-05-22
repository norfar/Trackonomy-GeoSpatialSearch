from sqlalchemy.orm import Session
import models
from database import engine

# Used for initializing location and device data for testing purposes
def init_data(db: Session):
    # Create tables if they don't exist
    models.Base.metadata.create_all(bind=engine)

    # Clear existing data from tables (this is only for testing)
    db.query(models.Location).delete()
    db.query(models.Device).delete()
    
    # Insert initial locations
    locations = [
        models.Location(location_id=1, location_name="San Jose", lat=37.3260883357, lon=-121.932892594, radius=20),
        models.Location(location_id=2, location_name="Atlanta", lat=33.7781026786, lon=-84.3967995323, radius=50)
    ]
    db.bulk_save_objects(locations)

    # Insert initial devices
    devices = [
        models.Device(device_id=1, device_name="Device 1", lat=37.3260883357, lon=-121.932892594),
        models.Device(device_id=2, device_name="Device 2", lat=37.3533207778, lon=-88.1844683419),
        models.Device(device_id=3, device_name="Device 3", lat=33.7631228124, lon=-84.3947361743),
        models.Device(device_id=4, device_name="Device 4", lat=33.7642571801, lon=-84.3957165021),
        models.Device(device_id=5, device_name="Device 5", lat=33.7663827025, lon=-84.3950806138)
    ]
    db.bulk_save_objects(devices)

    db.commit()
