# 📚 Book Recommender API

API backend avanzada construida con **FastAPI** y **MongoDB**, diseñada para recomendar libros de forma hiperpersonalizada combinando:

- 🎯 Un cuestionario literario sobre preferencias (géneros, emociones, estilo)
- 🧠 Un test de personalidad basado en el modelo Big Five (OCEAN)
- ⚙️ Un sistema de puntuación heurística para comparar perfiles con libros
- 📘 Un conjunto validado de 335 libros clasificados en 67 subgéneros

---

## 🚀 Tecnologías

- **FastAPI**
- **MongoDB (PyMongo)**
- **Pydantic**
- **dotenv**
- **Uvicorn**

---

## 📁 Estructura del proyecto

book_recommender_api/
├── app/
│   ├── main.py
│   ├── quiz.py
│   ├── personality.py
│   ├── profile.py
│   ├── recommender.py
│   ├── explain.py
│   ├── books_controller.py
│   ├── database.py
│   └── models.py
├── data/
│   └── books_all_335.json
├── utils/
│   ├── import_books.py
│   ├── validate_books.py
│   └── merge_books.py
├── requirements.txt
└── .env

---

## 🧪 Endpoints principales

| Método | Ruta                   | Descripción                                          |
|--------|------------------------|------------------------------------------------------|
| POST   | `/quiz`               | Enviar preferencias literarias del usuario           |
| POST   | `/personality-test`   | Enviar resultados del test Big Five (OCEAN)          |
| POST   | `/profile`            | Guardar perfil completo del usuario en MongoDB       |
| GET    | `/recommendation`     | Obtener libros más afines según el perfil            |
| GET    | `/explain-recommendation` | Justificación semántica de las recomendaciones |
| GET    | `/books`              | Lista de libros disponibles (título + autor)         |

---

## ⚙️ Cómo ejecutar el proyecto

# 1. Clonar el repositorio
https://github.com/tu_usuario/book-recommender-api.git

# 2. Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Crear archivo .env con:
MONGO_URI=mongodb://localhost:27017

# 5. Importar libros
python utils/import_books.py

# 6. Ejecutar el servidor
uvicorn app.main:app --reload

Accede a la documentación interactiva en:
👉 http://127.0.0.1:8000/docs

---

## 🧠 Ejemplo de perfil

{
  "preferences": {
    "genres": ["Fantasía", "Romance"],
    "themes": ["amistad", "superación"],
    "tone": "reflexivo",
    "style": "literario",
    "emotion_tags": ["esperanza", "tristeza"],
    "age_range": "14-18",
    "language": "es"
  },
  "personality": {
    "O": 82,
    "C": 65,
    "E": 47,
    "A": 74,
    "N": 32
  }
}

---

## ✅ Estado actual

- [x] API funcional con todos los endpoints clave
- [x] Sistema heurístico de recomendación preciso
- [x] Justificación semántica personalizada
- [x] Base de datos con 335 libros organizados


