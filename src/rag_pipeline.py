from src.pdf_loader import load_pdf
from src.chunking import split_text_with_overlap
from src.embeddings import create_embeddings, create_query_embedding
from src.vector_store import create_faiss_index, search_similar_chunks
from src.rag_answer import answer_with_context


def run_rag(pdf_paths, query):
    full_text = ""

    for pdf_path in pdf_paths:
        documents = load_pdf(pdf_path)

        for doc in documents:
            full_text += doc.page_content + "\n"

    chunks = split_text_with_overlap(
        full_text,
        chunk_size=100,
        overlap_fraction=0.2
    )

    embeddings = create_embeddings(chunks)

    index = create_faiss_index(embeddings)

    query_embedding = create_query_embedding(query)

    distances, indices = search_similar_chunks(index, query_embedding, top_k=5)

    context = "\n\n".join([chunks[i] for i in indices])

    answer = answer_with_context(query, context)

    return answer