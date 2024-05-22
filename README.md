# Trackonomy-GeoSpatialSearch
Geo-based search assignment for Trackonomy internship interview. 

Hi! Thanks again for this opportunity. This API implements a utility for finding what devices are within the radius of a given location. It does this with two tables in the backend, Locations and Devices. Please note that my code doesn't do anything with these tables other than initializing them with the data provided in the assignment document—the main function of my code is just the search function. 

## Setup

### Prerequisites

- Python 3.7 or higher
- PostgreSQL database

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/norfar/Trackonomy-GeoSpatialSearch/
   ```

2. Navigate to the project directory:

   ```bash
   cd Trackonomy-GeoSpatialSearch
   ```

3. Install dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. Update the database connection URL in the `database.py` file to point to your PostgreSQL database (mine is called GeoSpatialSearch).

2. For testing, you can modify the initial locations and devices data in the `init_db.py` file to suit your requirements.

### Running the Application

1. Start the FastAPI application:

   ```bash
   uvicorn main:app --reload
   ```

   This will start the FastAPI application and make it available at `http://localhost:8000`.

2. Run test cases using PyTest. I wrote a few in my test_main.py method. To run those, run:

   ```bash
   python3 -m pytest
   ```

