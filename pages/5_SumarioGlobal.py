import streamlit as st
import logging
from utils.pinecone_utils import get_all_docs
from utils.summarizer import summarize_global_docs

logger = logging.getLogger(__name__)

def app():
    logger.info("Entrando a SumarioGlobal")

    st.title("Sumario Global")
    st.write("Crea un sumario de todos los documentos indexados en Pinecone.")

    if st.button("Generar Sumario"):
        with st.spinner("Obteniendo todos los trozos e intentando un sumario..."):
            docs = get_all_docs()  # Te mostramos cómo implementarlo en pinecone_utils
            summary = summarize_global_docs(docs)
            st.success("Sumario generado:")
            st.write(summary)

def main():
    app()

if __name__ == "__main__":
    main()
