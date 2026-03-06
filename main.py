from pdf_loader import load_pdf
from chunking import split_text_with_overlap
from weaviate_store import create_client, recreate_collection, add_chunks

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

client = create_client()
collection = recreate_collection(client)

# store chunks in the vector database
add_chunks(collection, chunks)

count = collection.aggregate.over_all(total_count=True).total_count
print("Objects stored:", count)

client.close()