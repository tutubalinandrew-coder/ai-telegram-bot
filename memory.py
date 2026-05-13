from config import SYSTEM_PROMPT, MAX_HISTORY
from telegram.ext import ContextTypes
from repository import get_last_messages



def initialize_history(context: ContextTypes.DEFAULT_TYPE, user_id: int):
    if "messages" not in context.user_data:
        database_messages = load_messages_from_database(user_id)
        context.user_data["messages"] = [
            {"role": "system", "content": SYSTEM_PROMPT}
            ] + database_messages



def add_user_message(context: ContextTypes.DEFAULT_TYPE, text: str):
    context.user_data["messages"].append({"role": "user", "content": text})



def add_assistant_message(context: ContextTypes.DEFAULT_TYPE, ai_answer: str):
    context.user_data["messages"].append({"role": "assistant", "content": ai_answer})

def trim_history(context: ContextTypes.DEFAULT_TYPE):
    system_message = context.user_data["messages"][0]
    history = context.user_data["messages"][1:]
    context.user_data["messages"] = [system_message] + history[-MAX_HISTORY:]

def remove_last_user_message(context: ContextTypes.DEFAULT_TYPE):
    messages = context.user_data.get("messages", [])
    if messages and messages[-1]["role"] == "user":
        messages.pop()                

def get_messages(context: ContextTypes.DEFAULT_TYPE):
    return context.user_data["messages"]

def load_messages_from_database(user_id: int):
    messages = get_last_messages(user_id, 10)
    messages = messages[::-1]
    formatted_messages = []
    for role, message in messages:
        formatted_messages.append(
            {
            'role': role,
            'content': message
            }
        )
    return formatted_messages