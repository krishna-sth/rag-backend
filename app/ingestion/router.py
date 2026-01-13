from fastapi import APIRouter, UploadFile, File, Query
from app.ingestion.service import ingest_document

router = APIRouter(prefix="/ingest", tags=["Ingestion"])

@router.post("")
async def ingest(
    file: UploadFile = File(...),
    strategy: str = Query("fixed", enum=["fixed", "semantic"])
):
    return await ingest_document(file, strategy)
