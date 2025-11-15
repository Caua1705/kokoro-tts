from fastapi import FastAPI
from kokoro import TTS
from pydub import AudioSegment
import base64
import io

app = FastAPI()
tts = TTS("kokoro-small")

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/tts")
def tts_endpoint(text: str):
    audio = tts.generate(text)
    buffer = io.BytesIO()
    audio.export(buffer, format="mp3")
    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return {"audio": encoded}
