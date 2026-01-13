from fastapi import UploadFile
from app.ingestion.text_extractor import extract_text
from app.ingestion.chunking import fixed_chunk, semantic_chunk
from app.core.embeddings import embed_texts
from app.vectorstore.qdrant import upsert_chunks
from app.db.crud import save_document

async def ingest_document(file: UploadFile, strategy: str):
    text = extract_text(file)

    if strategy == "fixed":
        chunks = fixed_chunk(text)
    else:
        chunks = semantic_chunk(text)

    embeddings = embed_texts(chunks)

    upsert_chunks(chunks, embeddings)
    save_document(file.filename, len(chunks))

    return {
        "filename": file.filename,
        "chunks_stored": len(chunks),
        "strategy": strategy
    }
