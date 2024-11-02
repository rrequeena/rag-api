from pgvector.sqlalchemy import Vector
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Files(Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True)
    file_name = Column(String)
    file_content = Column(Text)

    chunks = relationship("FileChunks", back_populates="file")


class FileChunks(Base):
    __tablename__ = 'file_chunks'

    chunk_id = Column(Integer, primary_key=True)
    file_id = Column(Integer, ForeignKey('files.id'))
    chunk_text = Column(Text)
    embedding_vector: Vector = Column(Vector(1536))

    file = relationship("Files", back_populates="chunks")
