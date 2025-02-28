import streamlit as st
from utils.logging_config import setup_logging
import logging

def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    st.set_page_config(
        page_title="Document RAG App",
        page_icon="📄",
        layout="wide"
    )
    logger.info("Iniciando la app principal app.py")

    st.write("""
    # ¡Bienvenido al Document RAG App!
    Usa el menú lateral para:
    - Cargar documentos (PDF/TXT)
    - Chatear y hacer preguntas
    - Ver Ejemplos de preguntas
    - Sumario Global (opcional)
    """)

if __name__ == "__main__":
    main()
