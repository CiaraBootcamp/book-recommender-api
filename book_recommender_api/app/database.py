# ✅ database.py
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["book_recommender"]

# Devuelve el objeto base de la base de datos
def get_db():
    return db

# Devuelve directamente la colección de libros
def get_books_collection():
    return db["books"]
