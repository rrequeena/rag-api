FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
RUN chmod +x tools/init_local_db.sh
EXPOSE 8080
EXPOSE 9200
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]