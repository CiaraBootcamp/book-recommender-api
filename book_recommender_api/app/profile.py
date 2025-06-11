from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
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
users_collection = db["users"]

# 📌 MODELOS

class Preferences(BaseModel):
    genres: List[str]
    themes: List[str]
    tone: str
    style: str
    emotion_tags: List[str]
    age_range: str  # ⛔️ Se eliminó el campo language

class Personality(BaseModel):
    O: int
    C: int
    E: int
    A: int
    N: int

class UserBase(BaseModel):
    username: str
    email: EmailStr

class FullProfile(BaseModel):
    preferences: Preferences
    personality: Personality

# ✅ ENDPOINT: REGISTRAR USUARIO

@router.post("/register")
def register_user(user: UserBase):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Usuario ya registrado")
    
    user_data = user.dict()
    user_data["user_id"] = str(uuid4())
    user_data["created_at"] = datetime.utcnow().isoformat()
    user_data["preferences"] = None
    user_data["personality"] = None
    
    users_collection.insert_one(user_data)
    return {"message": "Usuario registrado correctamente", "user_id": user_data["user_id"]}

# ✅ ENDPOINT: AÑADIR QUIZ (preferencias)

@router.post("/add-quiz/{user_id}")
def add_quiz(user_id: str, preferences: Preferences):
    result = users_collection.update_one(
        {"user_id": user_id},
        {"$set": {"preferences": preferences.dict()}}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"message": "Preferencias guardadas correctamente"}

# ✅ ENDPOINT: AÑADIR TEST DE PERSONALIDAD

@router.post("/add-personality/{user_id}")
def add_personality(user_id: str, personality: Personality):
    result = users_collection.update_one(
        {"user_id": user_id},
        {"$set": {"personality": personality.dict()}}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"message": "Test de personalidad guardado correctamente"}

# ✅ ENDPOINT: CONSULTAR PERFIL COMPLETO

@router.get("/profile/{user_id}")
def get_profile(user_id: str):
    user = users_collection.find_one({"user_id": user_id}, {"_id": 0})
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user
