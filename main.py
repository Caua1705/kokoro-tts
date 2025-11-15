from fastapi import FastAPI
from kokoro_fastapi import KokoroEngine

app = FastAPI()
tts = KokoroEngine(model="small")  # versão leve compatível com Railway

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/speak")
def speak(text: str):
    audio_b64 = tts.generate_base64(text)
    return {
        "audio_base64": audio_b64
    }
