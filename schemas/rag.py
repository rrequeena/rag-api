from pydantic import BaseModel


class AskModel(BaseModel):
    document_id: int
    question: str