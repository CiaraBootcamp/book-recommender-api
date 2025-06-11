# recommender.py
from pymongo import MongoClient
from datetime import datetime
import uuid

client = MongoClient("mongodb://localhost:27017")
db = client["book_recommender"]


def match_personality(user_personality, book_tags):
    matched = 0
    for tag in book_tags:
        trait, level = tag.split()
        trait_key = trait[0].upper()
        value = user_personality.get(trait_key, 0)
        if (level == 'Alta' and value >= 70) or (level == 'Media' and 40 <= value < 70) or (level == 'Baja' and value < 40):
            matched += 1
    return matched / 5


def score_book(user, book):
    prefs = user["preferences"]
    genre_score = len(set(prefs["genres"]) & set(book["genres"])) / len(prefs["genres"] or [1])
    emotion_score = len(set(prefs["emotion_tags"]) & set(book["emotion_tags"])) / len(prefs["emotion_tags"] or [1])
    personality_score = match_personality(user["personality"], book["personality_match"])
    style_score = 1 if book["style"] == prefs["style"] else 0
    
    score = 0.4 * genre_score + 0.3 * emotion_score + 0.2 * personality_score + 0.1 * style_score
    return round(score, 4)


def generate_explanation(book, user):
    prefs = user["preferences"]
    reasons = []
    if book["style"] == prefs.get("style"):
        reasons.append(f"por su estilo {book['style']}")
    if set(book["emotion_tags"]) & set(prefs.get("emotion_tags", [])):
        reasons.append(f"por las emociones que evoca, como {', '.join(book['emotion_tags'][:2])}")
    if any(tag.startswith("Alta") for tag in book.get("personality_match", [])):
        reasons.append("por encajar con tu sensibilidad alta o tu perfil psicológico")
    return "Este libro fue seleccionado " + ", ".join(reasons) + "."