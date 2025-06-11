📚 PROYECTO COMPLETO: API de Recomendación de Libros Personalizada

---

🎯 VISIÓN GENERAL
Crear una plataforma backend avanzada (FastAPI + MongoDB) que recomiende libros hiperpersonalizados a partir de:

* Un cuestionario inteligente (gustos literarios, emociones, temas, estilo)
* Un test de personalidad psicológico (OCEAN – Big Five)
* Un sistema de puntuación heurística avanzado
* Un conjunto validado de 335 libros (5 por cada uno de los 67 subgéneros)

El objetivo es recomendar el **libro perfecto** para cada usuario, combinando afinidad emocional, temática y psicológica.

---

# 📘 README.md

## 📚 API DE RECOMENDACIÓN DE LIBROS PERSONALIZADA

Recomienda libros hiperpersonalizados combinando psicología (test OCEAN), preferencias literarias y un algoritmo heurístico sobre una base de 335 títulos organizados en 67 subgéneros.

---

## 🚀 FUNCIONALIDADES PRINCIPALES

* Cuestionario inteligente: preferencias literarias, emociones, estilo narrativo
* Test de personalidad Big Five (OCEAN)
* Generación de perfil lector completo
* Recomendación basada en puntuación heurística
* Explicación textual de cada recomendación

---

## ⚙️ TECNOLOGÍAS UTILIZADAS

* **FastAPI** – Backend principal
* **MongoDB** – Base de datos NoSQL (con PyMongo)
* **Python 3.11** – Lenguaje base
* **Postman o Streamlit** – Frontend de prueba (opcional)

---

## 🧱 ESTRUCTURA DEL PROYECTO

```
book_recommender_api/
├── app/
│   ├── main.py               # Inicializador FastAPI
│   ├── database.py           # Conexión a MongoDB
│   ├── models.py             # Esquemas Pydantic
│   ├── quiz.py               # Cuestionario de preferencias
│   ├── personality.py        # Test de personalidad OCEAN
│   ├── recommender.py        # Matching y explicación
│   ├── explain.py            # Justificación detallada
│   └── books_controller.py   # Carga y consulta de libros
├── data/
│   └── books_all_335.json    # Dataset de libros enriquecidos
├── utils/
│   ├── import_books.py       # Script de importación
│   └── ...                   # Herramientas auxiliares
├── requirements.txt          # Dependencias
└── README.md                 # Documentación
```

---

## 📌 ENDPOINTS PRINCIPALES

### POST `/quiz`

Envía las preferencias literarias del usuario.

### POST `/personality-test`

Envía las respuestas al test OCEAN (Big Five) y genera perfil psicológico.

### POST `/recommendation`

Combina preferencias y perfil OCEAN → Devuelve los libros más afines.

### GET `/explain-recommendation/{book_id}`

Explica por qué se ha recomendado ese libro.

---

## 🧠 EJEMPLO DE PERFIL DE USUARIO

```json
{
  "personality": { "O": 78, "C": 66, "E": 40, "A": 72, "N": 25 },
  "preferences": {
    "genres": ["Fantasía", "Romance"],
    "emotion_tags": ["esperanza", "suspenso"],
    "style": "literario",
    "tone": "reflexivo",
    "age_range": "14-18"
  }
}
```

---

## 📈 SISTEMA DE RECOMENDACIÓN

```python
score = (
    0.4 * genre_match +
    0.3 * emotion_match +
    0.2 * personality_match +
    0.1 * style_match
)
```

Cada libro es puntuado en función de su coincidencia con el perfil del usuario y ordenado por afinidad.

---

## 💬 EXPLICACIÓN AUTOMÁTICA

```json
{
  "book": "El Principito",
  "score": 0.87,
  "explanation": "Este libro fue seleccionado por su estilo poético, por las emociones que evoca, como nostalgia y ternura, y por encajar con tu sensibilidad alta y tu amor por la filosofía."
}
```

---

## ▶️ INSTRUCCIONES PARA EJECUTAR

1. Crear entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Cargar libros en MongoDB:

```bash
python utils/import_books.py
```

4. Ejecutar servidor:

```bash
uvicorn app.main:app --reload
```

5. Probar en navegador:

```
http://127.0.0.1:8000/docs
```


