# book_recommender_api/tests/test_recommender.py

import pytest
from book_recommender_api.app.models import FullProfile, Preferences, Personality
from book_recommender_api.app.recommender import compute_score, match_personality, generate_explanation, score_book

# 📘 Ejemplo de libro ficticio
mock_book = {
    "title": "Test Book",
    "author": "Author A",
    "genres": ["Ciencia Ficción", "Distopía"],
    "subgenres": ["Utopía"],
    "themes": ["libertad", "control social"],
    "emotion_tags": ["angustia", "alerta"],
    "tone": "oscuro",
    "style": "directo",
    "age_range": "16+",
    "personality_match": ["Alta apertura", "Alta extraversión"],
    "year": 2000,
    "description": "Un libro de prueba."
}

# 🧠 Perfil ficticio que debe coincidir parcialmente
mock_profile = FullProfile(
    preferences=Preferences(
        genres=["Ciencia Ficción"],
        themes=["libertad", "futurismo"],
        tone="oscuro",
        style="directo",
        emotion_tags=["alerta", "curiosidad"],
        age_range="16+",
        language="es"
    ),
    personality=Personality(O=75, C=55, E=80, A=50, N=30)
)


# 🔹 Test 1: compute_score
def test_compute_score():
    score = compute_score(mock_profile, mock_book)
    assert isinstance(score, float), "El resultado debe ser un número decimal"
    assert 0 <= score <= 1, "La puntuación debe estar entre 0 y 1"
    assert score > 0.3, "La puntuación debe reflejar al menos coincidencia parcial"


# 🔹 Test 2: match_personality
def test_match_personality():
    tags = ["Alta apertura", "Alta extraversión", "Alta amabilidad"]
    result = match_personality(mock_profile.personality, tags)
    assert 0 < result <= 1, "Debe haber al menos una coincidencia de personalidad"
    assert round(result, 2) == round(2 / 3, 2), "Coincidencias esperadas: 2 de 3"


# 🔹 Test 3: generate_explanation
def test_generate_explanation():
    explanation = generate_explanation(mock_book, mock_profile)
    assert isinstance(explanation, str)
    assert "géneros favoritos" in explanation
    assert "emociones evocadas" in explanation
    assert "estilo" in explanation


# 🔹 Test 4: score_book
def test_score_book():
    score = score_book(mock_book, mock_profile)
    assert abs(score - compute_score(mock_profile, mock_book)) < 1e-6
