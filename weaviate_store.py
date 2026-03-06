import weaviate
from weaviate.classes.config import Configure, Property, DataType

COLLECTION_NAME = "DocumentChunks"

# store Weaviate data locally
def create_client():
    client = weaviate.connect_to_embedded(
        persistence_data_path="./vectorstore"
    )
    return client

# recreate the collection during development to avoid duplicate chunks
def recreate_collection(client):

    if client.collections.exists(COLLECTION_NAME):
        client.collections.delete(COLLECTION_NAME)

    collection = client.collections.create(
        name=COLLECTION_NAME,
        properties=[
            Property(name="text", data_type=DataType.TEXT)
        ],
        vectorizer_config=Configure.Vectors.text2vec_transformers()
    )

    return collection

def add_chunks(collection, chunks):
    with collection.batch.fixed_size(batch_size=10) as batch:
        for chunk in chunks:
            batch.add_object(
                properties={"text": chunk}
            )