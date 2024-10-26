from fastapi import FastAPI, Depends

from sqlalchemy import select
from sqlalchemy.orm import Session

from database.db import engine, get_db, Base
from database.models import Files
from routers import upload_file_router, ask_question_router, similar_chunks_router

app = FastAPI(
    title="RAG API using OpenAI Models.",
    description="The API can upload, store and retrieve document information to be used with LLMs.",
    version="0.1",
)

Base.metadata.create_all(bind=engine)

@app.get('/')
async def root(db: Session = Depends(get_db)) -> list:
    """
    Get all the files in the database

    Returns:
    list: List of dictionaries containing the file_id and file_name
    """
    files_query = select(Files)
    files = db.scalars(files_query).all()
    files_lst = [
        {"file_id": file.id, "file_name": file.file_name}
        for file in files
    ]
    return files_lst

app.include_router(upload_file_router)
app.include_router(ask_question_router)
app.include_router(similar_chunks_router)
