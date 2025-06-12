# fetch_openlibrary_books.py
import requests
import json

SUBJECTS = ["science_fiction", "dystopia", "romance", "fantasy", "mystery"]
LIMIT = 100

books = []

for subject in SUBJECTS:
    url = f"https://openlibrary.org/subjects/{subject}.json?limit={LIMIT}"
    print(f"Fetching: {url}")
    resp = requests.get(url)
    data = resp.json()

    for work in data.get("works", []):
        books.append({
            "title": work.get("title"),
            "author": work.get("authors", [{}])[0].get("name", "Desconocido"),
            "subjects": work.get("subject", []),
            "description": work.get("description") if isinstance(work.get("description"), str) else "",
            "first_publish_year": work.get("first_publish_year")
        })

# Guardar JSON crudo
with open("book_recommender_api/data/books_openlibrary_raw.json", "w", encoding="utf-8") as f:
    json.dump(books, f, indent=4, ensure_ascii=False)

print(f"✅ Guardado books_openlibrary_raw.json con {len(books)} libros.")
