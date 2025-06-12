# import_books.py
import json
import os
from dotenv import load_dotenv
from book_recommender_api.app.database import get_books_collection

# Cargar variables de entorno
load_dotenv()

# Obtener colección
books_col = get_books_collection()

# ✅ NUEVA ruta al archivo enriquecido
BOOKS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "books_openlibrary_enriched.json")

def import_books():
    # Leer archivo
    with open(BOOKS_FILE, "r", encoding="utf-8") as f:
        books = json.load(f)

    # Validar
    if not isinstance(books, list):
        raise ValueError("El archivo JSON debe contener una lista de libros.")

    # Limpiar colección anterior
    books_col.delete_many({})

    # Insertar libros
    result = books_col.insert_many(books)
    print(f"✅ {len(result.inserted_ids)} libros importados correctamente.")

if __name__ == "__main__":
    import_books()
