from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv() 

# Retrieve database credentials from .env variables
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

# Construct the database URL
DATABASE_URL = "postgresql://" + USER + ":" + PASSWORD + "@localhost:5432/GeoSpatialSearch"

# Create a SQLAlchemy engine instance
engine = create_engine(DATABASE_URL)

# Create a sessionmaker instance bound to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a declarative base class for declarative models
Base = declarative_base()
