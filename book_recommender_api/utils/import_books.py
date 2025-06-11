# import_books.py
# utils/import_books.py

import json
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Configuración de MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["book_recommender"]
collection = db["books"]

# Ruta del archivo JSON
BOOKS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "books_all_335.json")

# Cargar libros y añadirlos a la colección
def import_books():
    with open(BOOKS_FILE, "r", encoding="utf-8") as f:
        books = json.load(f)

    if not isinstance(books, list):
        raise ValueError("El archivo JSON debe contener una lista de libros.")

    # Opcional: limpiar la colección antes de insertar
    collection.delete_many({})

    # Insertar libros
    result = collection.insert_many(books)
    print(f"✅ {len(result.inserted_ids)} libros importados correctamente.")

if __name__ == "__main__":
    import_books()
