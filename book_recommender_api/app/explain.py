# book_recommender_api/app/explain.py
from fastapi import APIRouter, HTTPException
from book_recommender_api.app.database import get_db  # ✅
from .recommender import compute_score
from bson.objectid import ObjectId

router = APIRouter()

def get_user_profile(user_id):
    db = get_db()
    return db["profiles"].find_one({"_id": ObjectId(user_id)})

@router.get("/explain-recommendation")
def explain_recommendation(user_id: str):
    db = get_db()
    user = get_user_profile(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    books = list(db["books"].find())
    explanations = []

    for book in books:
        score, matches = compute_score(user, book, explain=True)
        explanation = generate_explanation(book, matches)
        explanations.append({
            "book": book["title"],
            "score": round(score, 2),
            "matched": matches,
            "explanation": explanation
        })

    explanations.sort(key=lambda x: x["score"], reverse=True)
    return explanations[:5]  # top 5 libros recomendados

def generate_explanation(book, matches):
    parts = []
    if matches.get("genres"):
        parts.append(f"por incluir los géneros {', '.join(matches['genres'])}")
    if matches.get("emotions"):
        parts.append(f"por evocar emociones como {', '.join(matches['emotions'])}")
    if matches.get("style"):
        parts.append(f"por tener un estilo narrativo {matches['style']}")
    if matches.get("personality_tags"):
        parts.append(f"por coincidir con tu perfil psicológico: {', '.join(matches['personality_tags'])}")

    return "Este libro fue seleccionado " + ", ".join(parts) + "."
