# quiz.py
from fastapi import APIRouter, Body
from pydantic import BaseModel
from typing import List

router = APIRouter()

class UserPreferences(BaseModel):
    genres: List[str]
    themes: List[str]
    tone: str
    style: str
    emotion_tags: List[str]
    age_range: str
    language: str

@router.post("/quiz")
def submit_quiz(preferences: UserPreferences):
    return {"message": "Preferencias registradas", "preferences": preferences}