from pdf_loader import load_pdf
from chunking import split_text_with_overlap
from embeddings import create_embeddings, create_query_embedding
from vector_store import create_faiss_index, search_similar_chunks
from rag_answer import answer_with_context      

# load the selected PDFs and combine their text
while True:
    try:
        pdf_count = int(input("\n¿Cuántos PDFs quiere cargar? (1-3): "))

        if 1 <= pdf_count <= 3:
            break
        else:
            print("\nSolo puede cargar entre 1 y 3 PDFs. Intente nuevamente.\n")
    except ValueError:
        print("\nError: Ingrese un número válido entre 1 y 3.\n")

full_text = ""

for i in range(pdf_count):
    pdf_path = input(f"Ingrese la ruta del PDF {i + 1}: ")
    documents = load_pdf(pdf_path)
    
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

query = input("\nPregunta: ")
query_embedding = create_query_embedding(query)

distances, indices = search_similar_chunks(index, query_embedding, top_k=5)

# combine the retrieved chunks into one context
context = "\n\n".join([chunks[i] for i in indices])

answer = answer_with_context(query, context)

print("\nRespuesta:")
print(answer)

print(f"\n--- INFO DE PDFs CARGADOS ---")
print(f"Total de PDFs: {pdf_count}")
print(f"Total de caracteres combinados: {len(full_text)}")
print(f"Total de chunks generados: {len(chunks)}")
print("------------------------------")

print(f"\n--- CONTEXTO RECUPERADO (top {len(indices)} chunks) ---")
print(context)
print("-------------------------------------------------------")
