import os

from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

load_dotenv(find_dotenv())

FOLDER = "/docs"
OPENAI_KEY = os.getenv('OPENAI_API_KEY')

# OpenAI
OPENAI_CLIENT = OpenAI(api_key=OPENAI_KEY)

# Database credentials
POSTGRES_USERNAME = os.getenv('POSTGRES_USERNAME')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', "postgres")
POSTGRES_PORT = os.getenv('POSTGRES_PORT', 5432)
DATABASE_NAME = os.getenv('DATABASE_NAME', "rag_api_db")