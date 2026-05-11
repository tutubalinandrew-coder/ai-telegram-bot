

from itertools import count
from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ChatAction
from processor import process_user_message
from postgres_database import get_last_messages, delete_user_messages, count_user_messages
from datetime import datetime



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Чем могу помочь?")


async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    text = update.message.text
    user_id = update.effective_user.id

    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.TYPING
    )
    ai_answer = await process_user_message(context, user_id, text)
    await update.message.reply_text(ai_answer)


async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    context.user_data.pop("messages", None)
    delete_user_messages(user_id)
    await update.message.reply_text("История очищена")


async def history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    messages = get_last_messages(user_id, 6)
    messages = messages[::-1]
    if not messages:
        await update.message.reply_text("История пуста.")
        return
    history_text = ""
    for role, message in messages:
        history_text += f"{role.upper()}:\n{message}\n\n"
    if len(history_text) > 3500:
        history_text = history_text[:3500] + "\n... история обрезана"    
    await update.message.reply_text(history_text)

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current_time = datetime.now().strftime("%H:%M:%S")
    await update.message.reply_text(current_time)

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    count = count_user_messages(user_id)
    await update.message.reply_text(f"У Вас {count} сообщений в памяти.")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('''
    Введите одну из команд:
    /start
    /clear
    /history
    /stats
    /time
    /help'''
    )