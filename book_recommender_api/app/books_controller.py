from fastapi import APIRouter, HTTPException
from book_recommender_api.app.models import FullProfile, RecommendationResponse, BookOut
from book_recommender_api.app.database import get_books_collection
from book_recommender_api.app.recommender import compute_score, generate_explanation

# Aquí se inicializa el router
router = APIRouter()

# 🔹 Endpoint 1: Lista básica de libros
@router.get("/books")
def list_books():
    books_col = get_books_collection()
    books = list(books_col.find({}, {"_id": 0, "title": 1, "author": 1}))
    return books

# 🔹 Endpoint 2: Recomendación personalizada
@router.post("/recommendation", response_model=RecommendationResponse)
def recommend(profile: FullProfile):
    books_col = get_books_collection()

    # Filtro desactivado temporalmente para evitar dejar resultados vacíos
    query = {}

    books = list(books_col.find(query, {"_id": 0}))
    if not books:
        raise HTTPException(status_code=404, detail="No hay libros disponibles para recomendar.")

    # Calcular puntuaciones
    scored_books = [(book, compute_score(profile, book)) for book in books]
    scored_books = [pair for pair in scored_books if pair[1] > 0]

    if not scored_books:
        raise HTTPException(status_code=404, detail="Ningún libro coincide con tu perfil.")

    best_book, best_score = max(scored_books, key=lambda x: x[1])
    explanation = generate_explanation(best_book, profile)

    return RecommendationResponse(
        recommendation=BookOut(**best_book),
        explanation=explanation
    )
