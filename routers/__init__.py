from .ask_question_endpoint import router as ask_question_router
from .delete_document_endpoint import router as delete_document_router
from .similar_chunks_endpoint import router as similar_chunks_router
from .upload_file_endpoint import router as upload_file_router

__all__ = [
    "upload_file_router",
    "ask_question_router",
    "similar_chunks_router",
    "delete_document_router",
]
