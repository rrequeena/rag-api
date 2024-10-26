import os

from loguru import logger
from pgvector.sqlalchemy import Vector
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import text
from sqlalchemy_utils import database_exists, create_database

from utils.constants import (
    POSTGRES_USERNAME,
    POSTGRES_PASSWORD,
    POSTGRES_HOST,
    POSTGRES_PORT,
    DATABASE_NAME,
)
from database.models import Base

database_url = f"postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{DATABASE_NAME}"  # noqa
engine = create_engine(database_url)

if not database_exists(engine.url):
    create_database(engine.url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def get_db():
    """ Get the database session """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


with engine.begin() as conn:
    conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))

try:
    Base.metadata.create_all(engine)
except Exception as e:
    logger.debug(f"Error while creating tables: {e}")
