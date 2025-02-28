import streamlit as st
import logging

logger = logging.getLogger(__name__)

def app():
    logger.info("Entrando a Ejemplos")

    st.title("Ejemplos de Preguntas")

    example_questions = [
        "Resúmeme el capítulo 1",
        "Dame 3 conclusiones principales del PDF subido",
        "Explica la diferencia entre X y Y en el texto",
        "¿Qué metodología se describe en la sección 2?",
        "¿Cuáles son las conclusiones finales del autor?",
        "¿Qué ejemplos brinda para sustentar su argumento?",
        "Haz un resumen corto del documento (máx. 50 palabras)",
        "¿Qué limitaciones menciona el artículo?",
        "Compara la introducción y la discusión",
        "Dame 5 puntos clave del texto",
        "Explica brevemente la sección 'Resultados'",
        "¿Cómo define el autor el concepto de 'innovación'?",
        "¿Qué referencias son más relevantes?",
        "Resume el segundo capítulo en 3 oraciones",
        "¿Cuál es la postura principal del autor frente a X?",
        "¿Qué recomendaciones propone el texto al final?",
        "Dime una cita textual que respalde la hipótesis",
        "¿Cómo se relacionan los hallazgos con la teoría inicial?",
        "Explica la diferencia metodológica entre 'cuantitativo' y 'cualitativo' en el texto",
        "¿Qué implicaciones prácticas menciona para futuros estudios?"
    ]

    for q in example_questions:
        st.write(f"- {q}")

def main():
    app()

if __name__ == "__main__":
    main()
