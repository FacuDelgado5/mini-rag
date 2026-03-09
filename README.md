# Mini RAG System (Python + FAISS + Ollama)

A simple Retrieval-Augmented Generation (RAG) system built from scratch to understand how document question-answering systems work.

The project loads PDF documents, splits them into chunks, creates embeddings, retrieves relevant context using FAISS, and generates answers using a local LLM via Ollama.

The goal of this project is **learning and understanding the RAG pipeline step by step**, avoiding heavy frameworks that hide the internal logic.

---

# Features

- Load up to **3 PDF documents**
- Split text into overlapping chunks
- Generate embeddings using **Sentence Transformers**
- Perform semantic search with **FAISS**
- Retrieve the most relevant chunks
- Generate answers using **Mistral via Ollama**
- Two interfaces:
  - Console interface (`main.py`)
  - Web interface using **Streamlit** (`app.py`)

---

# Project Structure

```
mini-rag
│
├── app.py                # Streamlit interface
├── main.py               # Console interface
│
├── src
│   ├── __init__.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── pdf_loader.py
│   ├── vector_store.py
│   ├── rag_answer.py
│   └── rag_pipeline.py   # Main RAG pipeline
│
├── data                  # Example PDF
├── vectorstore           # Future storage for FAISS indexes
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# How the RAG Pipeline Works

```
PDF documents
↓
Text extraction
↓
Chunking (with overlap)
↓
Embeddings (sentence-transformers)
↓
Vector search (FAISS)
↓
Top-k chunk retrieval
↓
Context assembly
↓
LLM generation (Ollama / Mistral)
↓
Final answer
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/FacuDelgado5/mini-rag.git
cd mini-rag
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Ollama Setup

Install Ollama and download the model used in this project.

```bash
ollama pull mistral
```

Run the model locally:

```bash
ollama run mistral
```

---

# Running the Console Interface

```bash
python main.py
```

Example usage:

```
¿Cuántos PDFs quiere cargar? (1-3): 2
Ingrese la ruta del PDF 1: C:\Users\...\file1.pdf
Ingrese la ruta del PDF 2: C:\Users\...\file2.pdf

Pregunta: What is linear regression?

Respuesta:
...
```

---

# Running the Web Interface

```bash
streamlit run app.py
```

This will open the app in your browser.

The interface allows you to:

- Upload up to **3 PDFs**
- Ask questions about their content
- Receive generated answers based on the retrieved context

---

# Technologies Used

- Python
- Streamlit
- FAISS
- Sentence Transformers
- LangChain (only for PDF loading)
- Ollama
- Mistral LLM

---

# Learning Goals

This project is part of a personal AI learning roadmap.

It was built to apply concepts such as:

- embeddings
- semantic search
- vector databases
- Retrieval-Augmented Generation (RAG)
- integration of local language models

---

# Future Improvements

Possible improvements for this project:

- Persist FAISS indexes to disk
- Avoid recomputing embeddings
- Display retrieved chunks in the UI
- Improve prompt engineering
- Add support for more documents
- Add document metadata