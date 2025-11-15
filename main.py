from fastapi import FastAPI
from kokoro import TTS

app = FastAPI()
tts = TTS("kokoro-small")   # versão leve pro Railway

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/speak")
def speak(text: str):
    audio = tts.generate(text)
    return {
        "audio_base64": audio.to_base64()
    }
