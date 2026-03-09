import os
import tempfile
import time
import streamlit as st

from src.rag_pipeline import run_rag

st.set_page_config(
    page_title="Mini RAG",
    layout="centered"
)

st.title("Mini RAG")

uploaded_files = st.file_uploader(
    "Sube tus PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

question = st.text_area("Escribe tu pregunta")

if st.button("Generar respuesta", use_container_width=True):
    if not uploaded_files:
        st.warning("Debes subir al menos un PDF.")
    elif len(uploaded_files) > 3:
        st.warning("Solo puedes subir hasta 3 PDFs.")
    elif not question.strip():
        st.warning("Debes escribir una pregunta.")
    else:
        temp_paths = []

        try:
            start_time = time.time()

            with st.spinner("Procesando documentos y generando respuesta..."):
                for uploaded_file in uploaded_files:
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                        temp_file.write(uploaded_file.read())
                        temp_paths.append(temp_file.name)

                answer = run_rag(temp_paths, question)

            elapsed_time = time.time() - start_time

            st.success("Respuesta generada correctamente.")
            st.subheader("Respuesta")
            st.write(answer)
            st.caption(f"Tiempo de respuesta: {elapsed_time:.2f} segundos")

        except Exception as e:
            st.error(f"Ocurrió un error: {e}")

        finally:
            for path in temp_paths:
                if os.path.exists(path):
                    os.remove(path)