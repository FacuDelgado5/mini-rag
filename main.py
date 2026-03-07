from pdf_loader import load_pdf
from chunking import split_text_with_overlap
from embeddings import create_embeddings, create_query_embedding
from vector_store import create_faiss_index, search_similar_chunks
from rag_answer import answer_with_context      

# load the PDF and combine all pages
pdf_path = input("Ruta del PDF: ")
documents = load_pdf(pdf_path)

full_text = ""

for doc in documents:
    full_text += doc.page_content + "\n"

# split the document into overlapping chunks
chunks = split_text_with_overlap(
    full_text,
    chunk_size=100,
    overlap_fraction=0.2
)

# generate embeddings for each chunk
embeddings = create_embeddings(chunks)

# build the FAISS index
index = create_faiss_index(embeddings)

query = input("Pregunta: ")
query_embedding = create_query_embedding(query)

distances, indices = search_similar_chunks(index, query_embedding, top_k=3)

# combine the retrieved chunks into one context
context = "\n\n".join([chunks[i] for i in indices])

answer = answer_with_context(query, context)

print("Answer:")
print(answer)