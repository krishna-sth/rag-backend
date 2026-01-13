from fastapi import FastAPI
from app.vectorstore.qdrant import init_collection

app = FastAPI(title="RAG Backend")


@app.on_event("startup")
def startup_event():
    init_collection()


@app.get("/health")
def health():
    return {"status": "ok"}


from app.ingestion.router import router as ingestion_router

app.include_router(ingestion_router)

from app.rag.router import router as chat_router

app.include_router(chat_router)