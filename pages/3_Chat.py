import streamlit as st
import logging
from utils.pinecone_utils import search_docs
from utils.embedding_utils import generate_chat_response

logger = logging.getLogger(__name__)

def app():
    logger.info("Entrando a Chat con Historial")

    st.title("Chat con Documentos")

    if "chat_messages" not in st.session_state:
        st.session_state["chat_messages"] = []

    # Mostrar mensajes pasados
    for msg in st.session_state["chat_messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Pregunta o pide un resumen...")

    if user_input:
        # user
        st.session_state["chat_messages"].append({"role":"user","content":user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Buscar en Pinecone
        docs = search_docs(user_input)
        logger.info(f"Encontrados {len(docs)} docs para la query.")

        # Generar respuesta
        assistant_resp = generate_chat_response(docs, user_input)
        st.session_state["chat_messages"].append({"role":"assistant","content":assistant_resp})

        with st.chat_message("assistant"):
            st.markdown(assistant_resp)

def main():
    app()

if __name__ == "__main__":
    main()
