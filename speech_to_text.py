import assemblyai as aai
import asyncio
from config import speech_to_text_API_assemblyai, deepgram_API
from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)
# import wave
# import sys
# from vosk import Model, KaldiRecognizer, SetLogLevel


aai.settings.api_key = speech_to_text_API_assemblyai


async def speech_to_text_assemblyai(mp3_bytes):
    return aai.Transcriber().transcribe(mp3_bytes)


async def speech_to_text_deepgram(buffer_data):
    try:
        # STEP 1 Create a Deepgram client using the API key
        deepgram = DeepgramClient(deepgram_API)

        payload: FileSource = {
            "buffer": buffer_data,
        }
        # STEP 2: Configure Deepgram options for audio analysis
        options = PrerecordedOptions(
            model="nova-3",
            smart_format=True,
        )
        # STEP 3: Call the transcribe_file method with the text payload and options
        response = deepgram.listen.rest.v("1").transcribe_file(payload, options)
        result_dict = response.to_dict()
        transcript = result_dict["results"]["channels"][0]["alternatives"][0]["transcript"]
        return transcript
    except Exception as e:
        print(f"Exception: {e}")



# model_path = "vosk-model-en-us-0.22"
# model_vosk = Model(model_path)
#
async def vosk(audio):
    # SetLogLevel(0)
    #
    # wf = wave.open(sys.argv[1], "rb")
    # if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    #     print("Audio file must be WAV format mono PCM.")
    #     sys.exit(1)
#     rec = KaldiRecognizer(model_vosk, audio.getframerate())
#     rec.SetWords(True)
#     rec.SetPartialWords(True)
#
#     while True:
#         data = audio.readframes(4000)
#         if len(data) == 0:
#             break
#         if rec.AcceptWaveform(data):
#             print(rec.Result())
#         else:
#             print(rec.PartialResult())
#
#     print(rec.FinalResult())
    return