import os
from dotenv import load_dotenv

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
SYSTEM_PROMPT = "Ты - помощник, который помогает пользователю с его вопросами."
MAX_HISTORY = 20
ERROR_MESSAGE = "Не получилось получить ответ от AI. Попробуйте ещё раз чуть позже."
OPENAI_MODEL = "gpt-4o-mini"
