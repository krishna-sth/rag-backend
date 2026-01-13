from fastapi import APIRouter
from app.rag.service import chat

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("")
def chat_endpoint(session_id: str, message: str):
    return chat(session_id, message)
