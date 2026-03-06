from sentence_transformers import SentenceTransformer

# load the embedding model once so it can be reused
model = SentenceTransformer("all-MiniLM-L6-v2")

# convert text chunks into vector embeddings
def create_embeddings(chunks):
    return model.encode(chunks)

# convert a user question into a vector embedding
def create_query_embedding(query):
    return model.encode(query)