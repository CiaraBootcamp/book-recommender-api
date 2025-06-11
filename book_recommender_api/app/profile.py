from fastapi import APIRouter, Body
from pydantic import BaseModel
from typing import List
from datetime import datetime
from uuid import uuid4
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
router = APIRouter()

# Conexión a MongoDB
client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
db = client["book_recommender"]

class Preferences(BaseModel):
    genres: List[str]
    themes: List[str]
    tone: str
    style: str
    emotion_tags: List[str]
    age_range: str
    language: str

class Personality(BaseModel):
    O: int
    C: int
    E: int
    A: int
    N: int

class FullProfile(BaseModel):
    preferences: Preferences
    personality: Personality

@router.post("/profile")
def save_profile(profile: FullProfile):
    data = profile.dict()
    data["user_id"] = str(uuid4())
    data["timestamp"] = datetime.utcnow().isoformat()
    db["profiles"].insert_one(data)
    return {"message": "Perfil guardado", "user_id": data["user_id"]}