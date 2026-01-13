import redis
import os
from dotenv import load_dotenv

load_dotenv()

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    decode_responses=True
)

def get_history(session_id: str):
    return redis_client.lrange(session_id, 0, -1)

def save_message(session_id: str, role: str, message: str):
    redis_client.rpush(session_id, f"{role}: {message}")
