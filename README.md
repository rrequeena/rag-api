# RAG API 🤖 

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai)](https://openai.com)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org)
[![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com)

An API project for Retrieval-Augmented Generation (RAG) using OpenAI's models. This service enables document upload, storage, and intelligent querying using Large Language Models (LLMs).

## 🚀 Features

- Document upload and storage
- Text extraction and chunking
- Vector embeddings generation using OpenAI
- Semantic search capabilities
- Question answering with context
- Document management

## 🛠️ Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **OpenAI**: Embeddings and Language Models
- **PostgreSQL + pgvector**: Vector similarity search
- **Python 3.10+**: Modern Python features
- **Docker**: Containerization and deployment

## 🏃‍♂️ Quick Start

1. Clone the repository:
```bash
git clone https://github.com/rrequeena/rag-api.git
cd rag-api
```

2. Create a `.env` file with your configuration:
```env
OPENAI_API_KEY=sk-this-is-your-super-api-key
POSTGRES_USERNAME=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
DATABASE_NAME=rag_api_db
```
You will find a `.env.example` file at the project folder.

3. Start the services using Docker Compose:
```bash
docker-compose up --build
```

Or you can use Make commands:
```bash
make build
make compose
```

The API will be available at `http://localhost:8080`

## 🔗 API Endpoints

### GET /
Root endpoint that returns all the files stored in the DB.
```bash
curl -X 'GET' \
  'http://0.0.0.0:8080/' \
  -H 'accept: application/json'
```

### POST /uploadfile/
Upload a document for processing.
```bash
curl -X 'POST' \
  'http://0.0.0.0:8080/uploadfile/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@your_file.pdf;type=application/pdf'
```

### POST /ask/
Ask questions for a given document ID.
```bash
curl -X 'POST' \
  'http://0.0.0.0:8080/ask/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "document_id": 4,
  "question": "What is the document talking about?"
}'
```

### POST /find-similar-chunks/{file_id}
Find similar chunks of text for a given document.
```bash
curl -X 'POST' \
  'http://0.0.0.0:8080/find-similar-chunks/4' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "question": "Something you want to check"
}'
```

### DELETE /delete-document/{file_id}
Delete a document and its associated data.
```bash
curl -X DELETE "http://localhost:8080/delete-document/1" \
     -H "accept: application/json"
```

## 📝 Documentation

Full API documentation is available at:
- Swagger UI: `http://localhost:8080/docs`
