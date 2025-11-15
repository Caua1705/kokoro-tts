from fastapi import FastAPI
from pydub import AudioSegment
from kokoro_tts import Kokoro
import base64
import io

app = FastAPI()

tts = Kokoro("am_michael")

@app.post("/speak")
async def speak(payload: dict):
    text = payload.get("input", "")
    voice = payload.get("voice", "am_michael")

    wav_bytes = tts.generate(text, voice=voice)

    wav_audio = AudioSegment.from_file(io.BytesIO(wav_bytes), format="wav")
    mp3_buffer = io.BytesIO()
    wav_audio.export(mp3_buffer, format="mp3")
    mp3_bytes = mp3_buffer.getvalue()

    audio_base64 = base64.b64encode(mp3_bytes).decode("utf-8")

    return {"audio_base64": audio_base64}
