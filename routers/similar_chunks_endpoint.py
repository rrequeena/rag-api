from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.db import get_db
from schemas.basic import QuestionRequest
from utils.get_similar_chunks import get_similar_chunks

router = APIRouter()

@router.post("/find-similar-chunks/{file_id}")
async def find_similar_chunks_endpoint(
    file_id: int,
    question_data: QuestionRequest,
    db: Session = Depends(get_db)
) -> list:
    try:
        similar_chunks = await get_similar_chunks(file_id, question_data.question, db)

        formatted_response = [
            {"chunk_id": chunk.chunk_id, "chunk_text": chunk.chunk_text}
            for chunk in similar_chunks
        ]

        return formatted_response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
