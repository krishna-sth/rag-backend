from app.core.redis_client import get_history, save_message
from app.core.embeddings import embed_texts
from app.vectorstore.qdrant import search_chunks
from app.core.llm import call_llm
from app.booking.parser import extract_booking
from app.booking.service import save_booking

def chat(session_id: str, message: str):
    history = get_history(session_id)
    query_vector = embed_texts([message])[0]
    context = search_chunks(query_vector)

    prompt = f"""
Context:
{context}

Conversation:
{history}

User: {message}
"""

    response = call_llm(prompt)

    save_message(session_id, "user", message)
    save_message(session_id, "assistant", response)

    booking = extract_booking(message)
    if booking:
        save_booking(booking)

    return {"response": response}
