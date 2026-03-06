from pdf_loader import load_pdf
from chunking import split_text_with_overlap

# Load the PDF
documents = load_pdf("data/documento.pdf")

# Combine all pages into one text
full_text = ""

for doc in documents:
    full_text += doc.page_content + "\n"

# Create chunks
chunks = split_text_with_overlap(full_text, chunk_size=100, overlap_fraction=0.2)

print("Number of chunks:", len(chunks))
print()
print("First chunk:")
print(chunks[0])