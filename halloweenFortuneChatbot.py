import streamlit as st
import random
from huggingface_hub import InferenceClient


# Configurar la aplicación
st.set_page_config(page_title="Chatbot de Predicciones de Halloween", page_icon="🎃")

col1, col2 = st.columns(2)

with col1:
    st.image("logo-ief.png")

with col2:
    st.title("Bienvenido a la Cristal_IA del IEF 🔮")

st.markdown(
    "### Pregúntale a **Cristal_IA** por tu destino... Recuerda, ¡es solo por diversión!"
)

# Inicializar el cliente de Hugging Face
client = InferenceClient(api_key="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")


def generar_respuesta1(pregunta):
    messages = [
        {
            "role": "system",
            "content": "Eres un sabio oráculo que responde con humor y en español a las preguntas de los usuarios.",
        },
        {
            "role": "user",
            "content": f"Usuario: {nombre}, Profesión: {programa}. Pregunta: {pregunta}",
        },
    ]

    stream = client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct",
        # model="meta-llama/Llama-3.2-3B-Instruct",
        messages=messages,
        max_tokens=500,
        stream=True,
    )

    try:
        respuesta_modelo = ""
        for chunk in stream:
            respuesta_modelo += chunk.choices[0].delta.content
        # introduccion = random.choice(frases_introductorias)
        return f"{respuesta_modelo}"
    except Exception as e:
        return "Lo siento, los espíritus no pueden responder en este momento. Inténtalo de nuevo más tarde."


def generar_respuesta2(disfraz):
    messages = [
        {
            "role": "system",
            "content": "Eres un sabio oráculo que recomienda un disfraz con humor y en español a los usuarios.",
        },
        {
            "role": "user",
            "content": f"Usuario: {nombre}, Profesión: {programa}. Pregunta: {disfraz}",
        },
    ]

    stream = client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct",
        # model="meta-llama/Llama-3.2-3B-Instruct",
        messages=messages,
        max_tokens=400,
        stream=True,
    )

    try:
        respuesta_modelo = ""
        for chunk in stream:
            respuesta_modelo += chunk.choices[0].delta.content
        # introduccion = random.choice(frases_introductorias)
        return f"{respuesta_modelo}"
    except Exception as e:
        return "Lo siento, los espíritus no pueden responder en este momento. Inténtalo de nuevo más tarde."


# Campo de entrada para el usuario
nombre = st.text_input("¿Cuál es tu nombre?")
programa = st.text_input("¿Qué programa estudias o estudiaste?")
pregunta = st.text_input(
    "Haz tu pregunta a Cristal_IA (por ejemplo: ¿Qué me depara el futuro?)"
)

# Generar respuesta
if st.button("Consultar a Cristal_IA"):
    if pregunta:
        with st.spinner("Cristal_IA está observando tu destino..."):
            respuesta = generar_respuesta1(pregunta)
            st.write("\n" + respuesta)
    else:
        st.warning("Por favor, escribe una pregunta para consultar a Cristal_IA.")

st.write("¿Quieres una recomendación de disfraz?")

disfraz = "¿Qué disfraz puedo usar para Halloween?"

# Generar respuesta
if st.button("Recomendar disfraz"):
    if pregunta:
        with st.spinner("Cristal_IA está observando tu destino..."):
            respuesta = generar_respuesta2(pregunta)
            st.write("\n" + respuesta)
    else:
        st.warning("Por favor, escribe una pregunta para consultar a Cristal_IA.")


# Pie de página divertido
st.markdown("---")
st.markdown(
    "Recuerda: Las predicciones de **Cristal_IA** son solo para entretener y no deben tomarse en serio."
)

st.markdown(
    """Recuerda seguirnos en Instagram como [@institutoestudiosdelfuturo](https://www.instagram.com/institutoestudiosdelfuturo) y 
    compartir tu experiencia con el hashtag #cristal_IA. ¡Tenemos un dulce para ti 🍬! Acércate a la oficina EC-504 de la UdB"""
)

st.markdown("## Happy Hallow-IA 🎃 te desea el IEF!") 
