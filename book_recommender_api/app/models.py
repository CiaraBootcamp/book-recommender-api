# models.py
# ✅ models.py
from pydantic import BaseModel
from typing import List

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
