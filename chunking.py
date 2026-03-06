# split text into chunks with overlap.
def split_text_with_overlap(text, chunk_size=100, overlap_fraction=0.2):
    
    words = text.split()

    overlap = int(chunk_size * overlap_fraction)

    chunks = []

    for i in range(0, len(words), chunk_size):

        chunk_words = words[max(i - overlap, 0): i + chunk_size]

        chunk = " ".join(chunk_words)

        chunks.append(chunk)

    return chunks 