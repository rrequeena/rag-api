from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from utils.constants import OPENAI_CLIENT
from utils.get_similar_chunks import get_similar_chunks
from database.db import get_db
from schemas.rag import AskModel

router = APIRouter()

@router.post("/ask/")
async def ask_question(request: AskModel, db: Session = Depends(get_db)):
    """
    Ask a question and get a response using RAG

    Args:
    - request: AskModel - The request body containing the document_id and question
    - db: Session - The database session

    Returns:
    - dict: The response from the RAG model
    """
    try:
        similar_chunks = await get_similar_chunks(
            request.document_id, request.question, db
        )

        # Construct context from the similar chunks' texts
        context_texts = [chunk.chunk_text for chunk in similar_chunks]
        context = " ".join(context_texts)

        system_message = f"You are a helpful assistant. Here is the context to use to reply to questions: {context}"

        client = OPENAI_CLIENT
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": request.question},
            ],
        )

        return {"response": response.choices[0].message.content}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
