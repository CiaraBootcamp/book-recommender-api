import json
import os

# Ruta al archivo
CURRENT_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.normpath(os.path.join(CURRENT_DIR, "..", "data", "books_all_335.json"))

# Campos requeridos por libro
REQUIRED_FIELDS = [
    "title", "author", "genres", "subgenres", "themes", "emotion_tags",
    "tone", "style", "age_range", "language", "rating", "rating_source",
    "personality_match", "year", "isbn", "description"
]

# Validación
def validate_books(data):
    titles_seen = set()
    errors = []
    for idx, book in enumerate(data):
        book_id = f"{idx+1}: {book.get('title', '[NO TITLE]')}"
        
        # Verificar campos faltantes
        for field in REQUIRED_FIELDS:
            if field not in book:
                errors.append(f"❌ {book_id} → falta el campo '{field}'")

        # Verificar duplicados
        title = book.get("title", "").strip().lower()
        if title in titles_seen:
            errors.append(f"⚠️  Duplicado detectado: {book_id}")
        else:
            titles_seen.add(title)

    return errors

# Carga y ejecución
try:
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        books = json.load(f)
        print(f"📚 Libros cargados: {len(books)}")

    issues = validate_books(books)

    if issues:
        print("\n❗ Problemas encontrados:")
        for issue in issues:
            print(issue)
    else:
        print("✅ Todos los libros están correctamente estructurados y sin duplicados.")

except Exception as e:
    print(f"❌ Error al procesar el archivo: {e}")
