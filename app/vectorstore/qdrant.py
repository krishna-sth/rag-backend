from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
import os
from dotenv import load_dotenv

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")

COLLECTION_NAME = "documents"

client = QdrantClient(url=QDRANT_URL)


def init_collection(vector_size: int = 384):
    collections = client.get_collections().collections
    names = [c.name for c in collections]

    if COLLECTION_NAME not in names:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE
            )
        )


import uuid

def upsert_chunks(chunks, embeddings):
    points = []
    for chunk, vector in zip(chunks, embeddings):
        points.append({
            "id": str(uuid.uuid4()),
            "vector": vector,
            "payload": {"text": chunk}
        })

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

def search_chunks(query_vector, limit: int = 5):
    hits = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=limit
    )
    return [hit.payload["text"] for hit in hits]

