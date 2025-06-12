# enrich_books.py
import json
from random import choice, sample

with open("book_recommender_api/data/books_openlibrary_raw.json", "r", encoding="utf-8") as f:
    books = json.load(f)

def infer_emotions(subjects):
    mapping = {
        "Dystopia": ["angustia", "alerta"],
        "Romance": ["amor", "ternura"],
        "Fantasy": ["maravilla", "asombro"],
        "Mystery": ["suspenso", "curiosidad"]
    }
    emotions = []
    for subject in subjects:
        emotions += mapping.get(subject, [])
    return list(set(emotions))

enriched = []
for book in books:
    enriched.append({
        **book,
        "genres": book.get("subjects", [])[:2],
        "subgenres": book.get("subjects", [])[2:4],
        "themes": book.get("subjects", [])[4:6],
        "emotion_tags": infer_emotions(book.get("subjects", [])),
        "tone": choice(["oscuro", "luminoso", "reflexivo", "dinámico"]),
        "style": choice(["directo", "literario", "poético"]),
        "age_range": "16+",
        "personality_match": sample([
            "Alta apertura", "Alta amabilidad", "Bajo neuroticismo", 
            "Alta extraversión", "Alta responsabilidad"
        ], k=2),
        "year": book.get("first_publish_year", 0),
        "description": book.get("description", "")
    })

with open("book_recommender_api/data/books_all_extended.json", "w", encoding="utf-8") as f:
    json.dump(enriched, f, indent=4, ensure_ascii=False)

print(f"✅ Enriquecidos y guardados {len(enriched)} libros.")
