# models.py

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

class BookOut(BaseModel):
    title: str
    author: str
    genres: List[str]
    subgenres: List[str]
    themes: List[str]
    emotion_tags: List[str]
    tone: str
    style: str
    age_range: str
    personality_match: List[str]
    year: int
    description: str

class RecommendationResponse(BaseModel):
    recommendation: BookOut
    explanation: str
