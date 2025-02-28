import streamlit as st
import logging
from utils.doc_utils import parse_pdf, chunk_text
from utils.pinecone_utils import upsert_docs

logger = logging.getLogger(__name__)

def app():
    logger.info("Entrando a CargarDocumentos")

    st.title("Cargar Documentos")
    st.write("Sube PDFs/TXT, se indexarán en Pinecone para preguntas/resúmenes.")

    uploaded_files = st.file_uploader("Selecciona archivos", 
                                      type=["pdf","txt"], 
                                      accept_multiple_files=True)

    if st.button("Procesar e Indexar"):
        if not uploaded_files:
            st.warning("No subiste archivos.")
            logger.warning("Ningún archivo subido.")
            return

        st.info("Procesando e indexando en Pinecone...")

        all_chunks = []
        for f in uploaded_files:
            if f.name.endswith(".pdf"):
                text = parse_pdf(f)
            else:
                text = f.read().decode("utf-8", errors="ignore")

            # Trocear
            chunks = chunk_text(text, chunk_size=800)
            all_chunks.extend(chunks)

        upsert_docs(all_chunks)
        st.success("¡Documentos indexados con éxito!")
        logger.info(f"Indexados {len(all_chunks)} trozos en Pinecone.")

def main():
    app()

if __name__ == "__main__":
    main()
