# main.py
from fastapi import FastAPI
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# ✅ IMPORTS ABSOLUTOS
from book_recommender_api.app.quiz import router as quiz_router
from book_recommender_api.app.personality import router as personality_router
from book_recommender_api.app.explain import router as explain_router
from book_recommender_api.app.profile import router as profile_router

# ✅ Crea la app ANTES de registrar routers
app = FastAPI()
load_dotenv()

# Conexión MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["book_recommender"]

# Incluir routers
app.include_router(quiz_router)
app.include_router(personality_router)
app.include_router(explain_router)
app.include_router(profile_router)

@app.get("/")
def root():
    return {"message": "API de Recomendación de Libros activa"}

@app.get("/ping")
def ping():
    try:
        client.admin.command('ping')
        return {"status": "MongoDB conectado correctamente"}
    except Exception as e:
        return {"status": "Error de conexión", "error": str(e)}
