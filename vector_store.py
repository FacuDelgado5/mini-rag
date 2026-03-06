import faiss
import numpy as np

# create a FAISS index from the document embeddings
def create_faiss_index(embeddings):

    embeddings = np.array(embeddings, dtype="float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index

# search the most similar chunks to a query
def search_similar_chunks(index, query_embedding, top_k=3):

    query_embedding = np.array([query_embedding], dtype="float32")

    distances, indices = index.search(query_embedding, top_k)

    return distances[0], indices[0]