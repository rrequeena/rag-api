from fastapi import HTTPException
from openai import OpenAI
from sqlalchemy import select
from sqlalchemy.orm import Session

from utils.constants import OPENAI_CLIENT
from database.models import FileChunks


async def get_similar_chunks(
    file_id: int,
    question: str,
    db: Session
):
    """
    Get the most similar chunks to the question from the database

    Args:
    file_id (int): The file_id to search for the chunks
    question (str): The question to compare the chunks with
    db (Session): The database session

    Returns:
    list: List of similar chunks
    """
    try:
        response = OPENAI_CLIENT.embeddings.create(
            input=question,
            model="text-embedding-3-small"
        )
        question_embedding = response.data[0].embedding

        similar_chunks_query = select(FileChunks).where(FileChunks.file_id == file_id)\
            .order_by(FileChunks.embedding_vector.l2_distance(question_embedding)).limit(10)
        similar_chunks = db.scalars(similar_chunks_query).all()

        return similar_chunks

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
