from dotenv import load_dotenv
load_dotenv()
from pymongo import MongoClient
import os

DB_URL=os.environ.get('db_url')

conn = MongoClient(DB_URL)
db = conn.get_database("main_db")
Users = db.get_collection("users")

