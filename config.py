from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot_hub_API = os.getenv("bot_hub_API")
deepgram_API = os.getenv("deepgram_API")
deepseek_API = os.getenv("deepseek_API")
speech_to_text_API_assemblyai = os.getenv("speech_to_text_API_assemblyai")
