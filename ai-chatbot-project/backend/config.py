import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # .env 파일 로드

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
KAKAO_REST_API_KEY = os.getenv("KAKAO_REST_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY must be set in .env file")
