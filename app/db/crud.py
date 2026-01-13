from app.db.session import SessionLocal
from app.db.models import Document

def save_document(filename: str, chunk_count: int):
    db = SessionLocal()
    doc = Document(filename=filename, chunk_count=chunk_count)
    db.add(doc)
    db.commit()
    db.close()
