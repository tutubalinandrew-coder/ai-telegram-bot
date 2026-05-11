from telegram.ext import ContextTypes
from ai import get_ai_response
from memory import initialize_history, add_user_message, add_assistant_message, trim_history, remove_last_user_message, get_messages
from config import ERROR_MESSAGE
from logger import log_message
from postgres_database import save_message


async def process_user_message(context: ContextTypes.DEFAULT_TYPE, user_id: int, text: str):
    initialize_history(context, user_id)
    add_user_message(context, text)
    save_message(user_id, 'user', text)
    trim_history(context)
    ai_answer = await get_ai_response(get_messages(context))
    if ai_answer == ERROR_MESSAGE:
        remove_last_user_message(context)
        return ai_answer
    log_message(text, ai_answer)
    add_assistant_message(context, ai_answer)
    save_message(user_id, 'assistant', ai_answer)
    trim_history(context)
    return ai_answer