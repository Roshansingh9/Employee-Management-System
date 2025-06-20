from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


MONGODB_URL = os.getenv("MONGO_URL")  
if not MONGODB_URL:
    raise ValueError("Missing MONGODB_URL environment variable")
DATABASE_NAME = "keploy_db"


client = MongoClient(MONGODB_URL)
database = client[DATABASE_NAME]
employees_collection = database["employee"]

def get_database():
    return database

def get_employees_collection():
    return employees_collection