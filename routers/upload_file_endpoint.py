import io
import os
import shutil
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session

from utils.constants import FOLDER
from utils.background_tasks import TextProcessor
from utils.file_parser import FileParser
from database.db import get_db
from database.models import Files

router = APIRouter()

@router.post("/uploadfile/")
async def upload_file(
    background_tasks: BackgroundTasks,
    file: UploadFile,
    db: Session = Depends(get_db)
) -> dict:
    allowed_ext = ['txt', 'pdf']
    if file.filename.split('.')[-1] not in allowed_ext:
        exts = ", ".join(allowed_ext)
        raise HTTPException(
            status_code=400,
            detail=f"File type not allowed. Use only: {exts}" 
        )
    os.makedirs(FOLDER, exist_ok=True)

    try:
        file_path = os.path.join(FOLDER, file.filename)
        with open(file_path, "wb+") as f:
            content = await file.read()
            file_like_object = io.BytesIO(content)
            shutil.copyfileobj(file_like_object, f)

        content_parser = FileParser(file_path)
        file_text_content = content_parser.parse().replace("\x00", "")
        new_file = Files(file_name=file.filename,
                        file_content=file_text_content)
        db.add(new_file)
        db.commit()
        from loguru import logger
        logger.debug(f"Running background task")
        db.refresh(new_file)

        # Process the file in a background job
        background_tasks.add_task(
            TextProcessor(db, new_file.id).chunk_and_embed,
            file_text_content
        )

        return {
            "info": "File saved",
            "filename": file.filename
        }
    except Exception as e:
        print(f"Error while saving the file: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Something went wrong while saving the file: {e}"
        ) from e
