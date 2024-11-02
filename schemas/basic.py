from pydantic import BaseModel

class QuestionRequest(BaseModel):
    """Request body to recieve a question"""
    question: str
