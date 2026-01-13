from sentence_transformers import SentenceTransformer
from typing import List

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_texts(texts: List[str]) -> List[list]:
    return model.encode(texts).tolist()
