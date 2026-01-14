# Conversational RAG Backend

This project implements a backend system with document ingestion and a conversational Retrieval-Augmented Generation (RAG) API using FastAPI.

## Features

- Document Ingestion API
  - Upload PDF or TXT files
  - Text extraction and configurable chunking strategies
  - Embedding generation and storage in Qdrant
  - Metadata storage in PostgreSQL

- Conversational RAG API
  - Custom RAG implementation (no RetrievalQAChain)
  - Multi-turn conversations using Redis memory
  - Context-aware responses using stored document embeddings
  - Interview booking handled conversationally via LLM

## Tech Stack

- FastAPI
- PostgreSQL
- Qdrant
- Redis
- Docker & Docker Compose
- Google Gemini API (LLM)
- Python 3.10+

## Project Structure
```
app/
├── core/ # LLM configuration
├── db/ # Database models and CRUD
├── ingestion/ # Document ingestion logic
├── rag/ # Conversational RAG logic
├── vectorstore/ # Qdrant integration
├── main.py # FastAPI entry point
docker-compose.yml
```

## Setup Instructions

1. Clone the repository
```bash
git clone https://github.com/<username>/rag-backend.git
cd rag-backend
```

2. Create .env file
```
DATABASE_URL=postgresql://rag:rag@localhost:5432/ragdb
REDIS_URL=redis://localhost:6379
QDRANT_URL=http://localhost:6333
GOOGLE_API_KEY=your_api_key_here
```


3. Start services
```bash
docker-compose up -d
```

4. Run the application
```bash
uvicorn app.main:app --reload
```

5. Access API docs
```bash
http://localhost:8000/docs
```

## API Endpoints

- `POST /ingest`  
  Upload PDF or TXT documents for ingestion. The system extracts text, applies chunking, generates embeddings, and stores them in the vector database.

- `POST /chat`  
  Conversational RAG endpoint supporting multi-turn queries.  
  This endpoint also supports interview booking via natural language (name, email, date, time).

## Notes

- Interview booking is handled conversationally within the `/chat` endpoint using the LLM.
- No UI is included.
