from loguru import logger
from database.db import engine, SessionLocal

# Attempt to connect to the database and create a session
try:
    with engine.connect() as connection:
        logger.debug("Connected to the database successfully!")
        session = SessionLocal()
        logger.debug("Session created successfully!")
except Exception as e:
    logger.error(f"Error connecting to the database: {e}")
