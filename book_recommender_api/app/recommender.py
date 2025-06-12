# app/recommender.py

from typing import Dict
from .models import FullProfile, BookOut

# ---------------------
# 🔹 SCORE CALCULATION
# ---------------------

def compute_score(profile: FullProfile, book: Dict) -> float:
    preferences = profile.preferences

    # 1. Genre match (peso alto)
    genre_match = len(set(book.get("genres", [])) & set(preferences.genres))
    genre_score = genre_match / max(len(preferences.genres), 1) if genre_match > 0 else 0

    # 2. Theme match
    theme_match = len(set(book.get("themes", [])) & set(preferences.themes))
    theme_score = theme_match / max(len(preferences.themes), 1) if theme_match > 0 else 0

    # 3. Emotion match
    emotion_match = len(set(book.get("emotion_tags", [])) & set(preferences.emotion_tags))
    emotion_score = emotion_match / max(len(preferences.emotion_tags), 1) if emotion_match > 0 else 0

    # 4. Personality match (normalizado)
    personality_score = match_personality(profile.personality, book.get("personality_match", []))

    # 5. Tone and style match
    tone_match = 1.0 if book.get("tone") == preferences.tone else 0.0
    style_match = 1.0 if book.get("style") == preferences.style else 0.0

    # 6. Age range match
    age_match = 1.0 if book.get("age_range") == preferences.age_range else 0.0

    # Final weighted score (ajustado)
    score = (
        0.30 * genre_score +
        0.25 * theme_score +
        0.20 * emotion_score +
        0.15 * personality_score +
        0.05 * (tone_match + style_match) / 2 +
        0.05 * age_match
    )

    return round(score, 4)


# ---------------------
# 🔹 PERSONALITY MATCH
# ---------------------

def match_personality(personality: Dict, tags: list) -> float:
    """
    Calcula coincidencia de personalidad. Devuelve un valor entre 0 y 1.
    """
    score = 0
    if not tags:
        return 0.0

    for tag in tags:
        if "Alta apertura" in tag and personality.O >= 60:
            score += 1
        elif "Baja apertura" in tag and personality.O <= 40:
            score += 1
        elif "Alta responsabilidad" in tag and personality.C >= 60:
            score += 1
        elif "Baja responsabilidad" in tag and personality.C <= 40:
            score += 1
        elif "Alta extraversión" in tag and personality.E >= 60:
            score += 1
        elif "Baja extraversión" in tag and personality.E <= 40:
            score += 1
        elif "Alta amabilidad" in tag and personality.A >= 60:
            score += 1
        elif "Baja amabilidad" in tag and personality.A <= 40:
            score += 1
        elif "Alto neuroticismo" in tag and personality.N >= 60:
            score += 1
        elif "Bajo neuroticismo" in tag and personality.N <= 40:
            score += 1

    return round(score / len(tags), 4)


# ---------------------
# 🔹 EXPLANATION
# ---------------------

def generate_explanation(book: Dict, profile: FullProfile) -> str:
    matched_genres = set(book.get("genres", [])) & set(profile.preferences.genres)
    matched_themes = set(book.get("themes", [])) & set(profile.preferences.themes)
    matched_emotions = set(book.get("emotion_tags", [])) & set(profile.preferences.emotion_tags)

    explanation = f"Este libro fue seleccionado por coincidir con tus géneros favoritos ({', '.join(matched_genres)}), "
    explanation += f"temas como ({', '.join(matched_themes)}), "
    explanation += f"emociones evocadas ({', '.join(matched_emotions)}), "
    explanation += f"y por su estilo {book.get('style')} y tono {book.get('tone')}."

    return explanation


# ---------------------
# 🔹 PUBLIC INTERFACE
# ---------------------

def score_book(book: Dict, profile: FullProfile) -> float:
    """
    Interfaz pública para calcular la puntuación de un libro.
    """
    return compute_score(profile, book)
