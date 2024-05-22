from fastapi.testclient import TestClient
from fastapi import status
from main import app

# Create a test client instance
client = TestClient(app=app)

# Tests endpoint to get all locations
def test_get_locations(): 
    response = client.get('/locations')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {"location_id": 1, "location_name": "San Jose", "lat": 37.3260883357, "lon": -121.932892594, "radius": 20.0}, 
        {"location_id": 2, "location_name": "Atlanta", "lat": 33.7781026786, "lon": -84.3967995323, "radius": 50.0}
        ]

# Tests endpoint to get all devices
def test_get_devices(): 
    response = client.get('/devices')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {"device_id": 1, "device_name": "Device 1", "lat": 37.3260883357, "lon": -121.932892594}, 
        {"device_id": 2, "device_name": "Device 2", "lat": 37.3533207778, "lon": -88.1844683419}, 
        {"device_id": 3, "device_name": "Device 3", "lat": 33.7631228124, "lon": -84.3947361743}, 
        {"device_id": 4, "device_name": "Device 4", "lat": 33.7642571801, "lon": -84.3957165021}, 
        {"device_id": 5, "device_name": "Device 5", "lat": 33.7663827025, "lon": -84.3950806138}
        ]

# Tests search endpoint to for valid searches
def test_valid_searches(): 
    response = client.get('/search/1')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "location_id": 1, 
        "found_devices": ["Device 1"]
        }

    response = client.get('/search/2')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "location_id": 2, 
        "found_devices": ["Device 3", "Device 4", "Device 5"]
        }

# Tests search endpoint for a location_id that doesn't exist in the location table
def test_invalid_location_id(): 
    response = client.get('/search/5')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": "Location not found"
        }
    
# Tests search endpoint for a location_id that is a non-integer value
def test_invalid_non_integer_id():
    # If the location_id is a string
    response = client.get('/search/abc')
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": [
            {
            "type": "int_parsing",
            "loc": [
                "path",
                "location_id"
            ],
            "msg": "Input should be a valid integer, unable to parse string as an integer",
            "input": "abc"
            }
        ]
        }
    
    # If the location_id is a float
    response = client.get('/search/1.2')
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": [
            {
            "type": "int_parsing",
            "loc": [
                "path",
                "location_id"
            ],
            "msg": "Input should be a valid integer, unable to parse string as an integer",
            "input": "1.2"
            }
        ]
        }

# Tests search endpoint with no parameters 
def test_invalid_empty_search():
    response = client.get('/search')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": "Not Found"
        }

# Tests search endpoint with mutliple parameters 
def test_invalid_empty_search():
    response = client.get('/search/1/2')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": "Not Found"
        }