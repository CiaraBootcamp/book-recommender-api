# ✅ books_controller.py
from fastapi import APIRouter
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
router = APIRouter()

client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
db = client["book_recommender"]

@router.get("/books")
def list_books():
    books = list(db["books"].find({}, {"_id": 0, "title": 1, "author": 1}))
    return books