from typing import List

def fixed_chunk(text: str, size: int = 500, overlap: int = 50) -> List[str]:
    chunks = []
    start = 0
    while start < len(text):
        end = start + size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks


def semantic_chunk(text: str) -> List[str]:
    paragraphs = text.split("\n\n")
    return [p.strip() for p in paragraphs if len(p.strip()) > 100]
