FROM python:3.10-slim

RUN apt-get update && apt-get install -y git && apt-get clean

WORKDIR /app

RUN pip install fastapi uvicorn[standard] kokoro-lite

COPY main.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
