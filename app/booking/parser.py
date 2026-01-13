import json
from app.core.llm import call_llm

BOOKING_PROMPT = """
If the user wants to book an interview, extract:
name, email, date, time

Return STRICT JSON or return null.
"""

def extract_booking(message: str):
    result = call_llm(BOOKING_PROMPT + message)
    try:
        return json.loads(result)
    except:
        return None
