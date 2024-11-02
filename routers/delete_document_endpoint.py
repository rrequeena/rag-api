from fastapi import APIRouter, Depends, HTTPException

from database.db import get_db
from database.models import Files

router = APIRouter()

@router.delete("/delete-document/{file_id}")
async def delete_document(file_id: int, db=Depends(get_db)) -> dict:
    """
    Delete a document from the database

    Args:
    - file_id: int - The ID of the document to delete
    - db: Session - The database session

    Returns:
    - dict: The response message
    """
    try:
        file = db.query(Files).filter(Files.id == file_id).first()
        if not file:
            raise HTTPException(status_code=404, detail="File not found")
        db.delete(file)
        db.commit()
        return {"info": "Document deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
