from fastapi import FastAPI
from kokoro_lite import KokoroTTS

app = FastAPI()
tts = KokoroTTS()

@app.get("/")
def ping():
    return {"ok": True}

@app.get("/speak")
def speak(text: str):
    audio = tts.generate(text)
    return {"audio_base64": audio.to_base64()}
