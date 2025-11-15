from fastapi import FastAPI
from pydub import AudioSegment
from kokoro import TTS
import base64
import io

app = FastAPI()

tts = TTS("kokoro")  # modelo original

@app.post("/speak")
async def speak(payload: dict):
    text = payload.get("input", "")
    voice = payload.get("voice", "am_michael")

    audio_pcm = tts.generate(text, voice=voice).audio  # PCM WAV raw bytes

    # Converter PCM para MP3 usando pydub
    wav_audio = AudioSegment(
        data=audio_pcm,
        sample_width=2,
        frame_rate=24000,
        channels=1
    )
    mp3_buffer = io.BytesIO()
    wav_audio.export(mp3_buffer, format="mp3")
    mp3_bytes = mp3_buffer.getvalue()

    audio_base64 = base64.b64encode(mp3_bytes).decode("utf-8")

    return {"audio_base64": audio_base64}
