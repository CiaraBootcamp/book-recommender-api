import streamlit as st
import requests

# Configuración de la página
st.set_page_config(page_title="Recomendador de Libros", layout="centered")

# Título de la aplicación
st.title("📚 Recomendador Personalizado de Libros")
st.subheader("Contesta el siguiente cuestionario para obtener una recomendación literaria única.")

# ---------------------------
# 1. Cuestionario literario
# ---------------------------
st.header("🎯 Tus preferencias literarias")

# Preguntas para las preferencias literarias
genre = st.multiselect("¿Qué géneros te gustan?", ["Ciencia Ficción", "Fantasía", "Drama", "Romance", "Filosofía", "Misterio"])
themes = st.multiselect("¿Qué temas te interesan?", ["amistad", "superación personal", "control social", "existencialismo", "familia"])
tone = st.selectbox("¿Qué tono prefieres?", ["oscuro", "luminoso", "reflexivo", "dinámico"])
style = st.selectbox("¿Qué estilo narrativo prefieres?", ["directo", "poético", "literario"])
emotion_tags = st.multiselect("¿Qué emociones te gusta que evoque un libro?", ["esperanza", "tristeza", "reflexión", "ternura", "angustia"])
age_range = st.selectbox("¿Cuál es tu rango de edad preferido para los libros?", ["16+", "18+"])
language = st.selectbox("¿En qué idioma prefieres leer?", ["es", "en"])

# ---------------------------
# 2. Test Big Five (OCEAN)
# ---------------------------
st.header("🧠 Test de Personalidad Big Five")

# Diccionario de respuestas de likert
likert = {
    "Muy en desacuerdo": 1,
    "En desacuerdo": 2,
    "Neutral": 3,
    "De acuerdo": 4,
    "Muy de acuerdo": 5
}

st.markdown("Responde del 1 (Muy en desacuerdo) al 5 (Muy de acuerdo):")

# Preguntas del test Big Five
O = likert[st.radio("Me gusta experimentar cosas nuevas y tengo mucha imaginación.", list(likert.keys()), key="O1")]
O += likert[st.radio("Disfruto aprendiendo sobre temas filosóficos o abstractos.", list(likert.keys()), key="O2")]

C = likert[st.radio("Soy organizado y me gusta planificar con antelación.", list(likert.keys()), key="C1")]
C += likert[st.radio("Cumplo mis responsabilidades con disciplina.", list(likert.keys()), key="C2")]

E = likert[st.radio("Disfruto interactuando con la gente y soy sociable.", list(likert.keys()), key="E1")]
E += likert[st.radio("Me siento lleno de energía cuando estoy rodeado de personas.", list(likert.keys()), key="E2")]

A = likert[st.radio("Me preocupo por los demás y trato de ayudar.", list(likert.keys()), key="A1")]
A += likert[st.radio("Confío en los demás y soy cooperativo.", list(likert.keys()), key="A2")]

N = likert[st.radio("Me estreso con facilidad.", list(likert.keys()), key="N1")]
N += likert[st.radio("A menudo me siento ansioso o inseguro.", list(likert.keys()), key="N2")]

# Convertir a escala de 0 a 100
def scale(val): return int((val / 10) * 100)

# Resultado del test de personalidad
personality = {
    "O": scale(O),
    "C": scale(C),
    "E": scale(E),
    "A": scale(A),
    "N": scale(N),
}

# ---------------------------
# 3. Enviar a API
# ---------------------------
if st.button("🔍 Obtener recomendación"):
    # Crear payload con las respuestas del cuestionario
    payload = {
        "preferences": {
            "genres": genre,
            "themes": themes,
            "tone": tone,
            "style": style,
            "emotion_tags": emotion_tags,
            "age_range": age_range,
            "language": language
        },
        "personality": personality
    }

    try:
        # Realizar la petición a la API de recomendación
        response = requests.post("http://127.0.0.1:8001/api/recommendation", json=payload)
        if response.status_code == 200:
            data = response.json()["recommendation"]
            # Mostrar los resultados
            st.success("✅ ¡Libro recomendado!")
            st.markdown(f"### **{data['title']}**\n📖 *{data['author']}*\n\n🧠 _{data['description']}_")
            st.markdown(f"**Motivo:** {response.json()['explanation']}")
        else:
            st.error(f"⚠️ {response.json()['detail']}")
    except Exception as e:
        st.error("🚫 Error al conectar con la API.")
        st.text(str(e))
