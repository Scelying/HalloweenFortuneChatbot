import streamlit as st
import random
from huggingface_hub import InferenceClient


# Configurar la aplicación
st.set_page_config(page_title="Chatbot de Predicciones de Halloween", page_icon="🎃")

col1, col2 = st.columns(2)

with col1:
    st.image("logo-ief.png")

with col2:
    st.title("🔮 Bienvenido al Oráculo de Halloween 🔮")

st.write("Pregúntale al Oráculo tu destino... pero recuerda, ¡es solo por diversión!")

# Inicializar el cliente de Hugging Face
client = InferenceClient(api_key="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")

def generar_respuesta(pregunta):
    messages = [
        {"role": "system", "content": "Eres un sabio oráculo que responde con humor y en español a las preguntas de los usuarios."},
        {"role": "user", "content": f"Usuario: {nombre}, Profesión: {programa}. Pregunta: {pregunta}"}
    ]

    stream = client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct",
        #model="meta-llama/Llama-3.2-3B-Instruct",
        messages=messages,
        max_tokens=500,
        stream=True,
    )
    
    try:
        respuesta_modelo = ""
        for chunk in stream:
            respuesta_modelo += chunk.choices[0].delta.content
        #introduccion = random.choice(frases_introductorias)
        return f"{respuesta_modelo}"
    except Exception as e:
        return "Lo siento, los espíritus no pueden responder en este momento. Inténtalo de nuevo más tarde."

# Campo de entrada para el usuario
nombre = st.text_input("¿Cuál es tu nombre?")
programa = st.text_input("¿Qué programa estudias o estudiaste?")
pregunta = st.text_input(
    "Haz tu pregunta al Oráculo (por ejemplo: ¿Qué me depara el futuro?)"
)

# Generar respuesta
if st.button("Consultar el Oráculo"):
    if pregunta:
        with st.spinner("El Oráculo está observando tu destino..."):
            respuesta = generar_respuesta(pregunta)
            st.write("\n" + respuesta)
    else:
        st.warning("Por favor, escribe una pregunta para consultar al Oráculo.")

# Pie de página divertido
st.markdown("---")
st.write(
    "Recuerda: Las predicciones del Oráculo son solo para entretener y no deben tomarse en serio. ¡Feliz Halloween!"
)