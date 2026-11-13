from gtts import gTTS
# from vosk import Model, KaldiRecognizer
# import wave
from pydub import AudioSegment
import json
from io import BytesIO
import asyncio
from config import deepgram_API
import requests
from deepgram import DeepgramClient, SpeakOptions
import random as r


async def google_text_to_speech(text, lang):
    audio_buffer = BytesIO()
    tts = gTTS(text=text, lang=lang)
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer


async def deepgram_text_to_speech(text, model):
    try:
        deepgram = DeepgramClient(deepgram_API)

        # Настройки голоса
        options = SpeakOptions(
            model=model,
        )
        speak_options = {"text": text}

        response = deepgram.speak.v("1").stream(speak_options, options)
        # Get the audio stream from the response
        audio_buffer = BytesIO(response.stream.read())
        audio_buffer.seek(0)
        # Возвращаем файл для Telegram
        return audio_buffer

    except Exception as e:
        print(f"Exception: {e}")