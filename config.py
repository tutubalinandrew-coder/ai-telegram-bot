import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
if not BOT_TOKEN:
    raise ValueError('Ошибка - бот_токен отсутствует')
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
if not OPENAI_API_KEY:
    raise ValueError('Ошибка - OPENAI_API_KEY отсутствует')
SYSTEM_PROMPT = "Ты - помощник, который помогает пользователю с его вопросами."
MAX_HISTORY = 20
ERROR_MESSAGE = "Не получилось получить ответ от AI. Попробуйте ещё раз чуть позже."
OPENAI_MODEL = "gpt-4o-mini"
POSTGRES_DB = os.environ.get("POSTGRES_DB", "")
POSTGRES_USER = os.environ.get("POSTGRES_USER", "")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT", "")