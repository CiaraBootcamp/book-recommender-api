# main.py
from fastapi import FastAPI
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# ✅ IMPORTS DE TODOS LOS ROUTERS
from book_recommender_api.app.quiz import router as quiz_router
from book_recommender_api.app.personality import router as personality_router
from book_recommender_api.app.explain import router as explain_router
from book_recommender_api.app.profile import router as profile_router
from book_recommender_api.app.books_controller import router as books_router  # 🔥 AÑADIDO
# Si luego usas `recommendations_router`, aquí también se importa

# ✅ Carga de variables y creación de app
load_dotenv()
app = FastAPI(title="Book Recommender API")

# Conexión MongoDB para test de salud (no obligatorio aquí si usas get_db en routers)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)

# ✅ Inclusión de todos los routers con prefijo si se desea
app.include_router(quiz_router, prefix="/quiz")
app.include_router(personality_router, prefix="/personality")
app.include_router(explain_router, prefix="/explain")
app.include_router(profile_router, prefix="/profile")
app.include_router(books_router, prefix="/api")  # 📚 NUEVO ENDPOINT

# ✅ Raíz
@app.get("/")
def root():
    return {"message": "API de Recomendación de Libros activa"}

# ✅ Endpoint de salud (versión robusta)
@app.get("/health")
def health_check():
    try:
        client.admin.command('ping')
        return {"status": "ok", "mongodb": "conectado"}
    except Exception as e:
        return {"status": "error", "mongodb": "no conectado", "error": str(e)}
