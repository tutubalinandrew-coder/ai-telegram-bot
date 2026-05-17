import os
from dotenv import load_dotenv

load_dotenv(override=True)

def get_env(name):
    env = os.environ.get(name)
    if not env:
         raise ValueError(f'Ошибка - {name} отсутствует')
    return env

BOT_TOKEN = get_env("BOT_TOKEN")


OPENAI_API_KEY = get_env("OPENAI_API_KEY")

SYSTEM_PROMPT = "Ты - помощник, который помогает пользователю с его вопросами."
MAX_HISTORY = 20
ERROR_MESSAGE = "Не получилось получить ответ от AI. Попробуйте ещё раз чуть позже."
OPENAI_MODEL = get_env("OPENAI_MODEL")
POSTGRES_DB = get_env("POSTGRES_DB")
POSTGRES_USER = get_env("POSTGRES_USER")
POSTGRES_PASSWORD = get_env("POSTGRES_PASSWORD")
POSTGRES_HOST = get_env("POSTGRES_HOST")
POSTGRES_PORT = get_env("POSTGRES_PORT")
RATE_LIMIT = 3
MEMORY_LIMIT = 2