import nltk
from nltk.tokenize import sent_tokenize
from openai import OpenAI
from sqlalchemy.orm import Session

from utils.constants import OPENAI_CLIENT
from database.models import FileChunks

nltk.download('punkt')


class TextProcessor:
    """ Process text and generate embeddings for the chunks """
    def __init__(self, db: Session, file_id: int, chunk_size: int = 2):
        self.db = db
        self.file_id = file_id
        self.chunk_size = chunk_size

    def chunk_and_embed(self, text: str) -> None:
        """
        Generate embeddings for a given text and chunk it.

        Args:
            text: str
            The text to generate the embeddings and make into chunks
        
        Returns:
            None
        """
        sentences = sent_tokenize(text)
        chunks = [
            ' '.join(sentences[i:i + self.chunk_size])
            for i in range(0, len(sentences), self.chunk_size)
        ]

        # Create and store embeddings
        for chunk in chunks:
            response = OPENAI_CLIENT.embeddings.create(
                model='text-embedding-3-small',
                input=chunk
            )
            embedding = response.data[0].embedding
            file_chunk = FileChunks(
                file_id=self.file_id,
                chunk_text=chunk,
                embedding_vector=embedding
            )
            self.db.add(file_chunk)
        self.db.commit()
