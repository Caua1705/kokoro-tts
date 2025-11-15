FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    ffmpeg \
    curl \
    unzip \
    build-essential \
    python3-dev \
    && apt-get clean

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY install_kokoro.sh .
RUN chmod +x install_kokoro.sh && ./install_kokoro.sh

COPY main.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
