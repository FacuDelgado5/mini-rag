from pdf_loader import load_pdf
from chunking import split_text_with_overlap
from embeddings import create_embeddings, create_query_embedding
from vector_store import create_faiss_index, search_similar_chunks

# load the PDF and combine all pages
documents = load_pdf("data/documento.pdf")

full_text = ""

for doc in documents:
    full_text += doc.page_content + "\n"

# split the document into overlapping chunks
chunks = split_text_with_overlap(
    full_text,
    chunk_size=100,
    overlap_fraction=0.2
)

print("Number of chunks:", len(chunks))

# generate embeddings for each chunk
embeddings = create_embeddings(chunks)

print("Number of embeddings:", len(embeddings))
print("Embedding dimension:", len(embeddings[0]))

# build the FAISS index
index = create_faiss_index(embeddings)

query = "¿Qué es la regresión lineal?"
query_embedding = create_query_embedding(query)

distances, indices = search_similar_chunks(index, query_embedding, top_k=3)

print()
print("Query:", query)
print()

print("Most relevant chunks:")
for i, chunk_index in enumerate(indices, start=1):
    print(f"Chunk {i}:")
    print(chunks[chunk_index])
    print()
    
# combine the retrieved chunks into one context
context = "\n\n".join([chunks[i] for i in indices])

print("Context:")
print(context)