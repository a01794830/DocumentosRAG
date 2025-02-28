import streamlit as st
import logging

logger = logging.getLogger(__name__)

def app():
    logger.info("Entrando a Home")

    st.title("Document RAG App - Home")
    st.write("""
    Bienvenido. Aquí podrás subir PDFs/TXT, generar embeddings en Pinecone 
    y consultarlos con OpenAI. 
    Disfruta de funciones de sumario y chat RAG.
    """)

def main():
    app()

if __name__ == "__main__":
    main()
