from pdf_loader import load_pdf
from chunking import split_text_with_overlap
from embeddings import create_embeddings

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

print()
print("First chunk:")
print(chunks[0])

print()
print("First embedding (first values):")
print(embeddings[0][:10])

