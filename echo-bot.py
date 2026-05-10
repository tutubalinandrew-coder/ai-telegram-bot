from telegram.constants import ChatAction
from telegram import Update
from telegram.ext import (Application, CommandHandler, MessageHandler, ContextTypes, filters)
from openai import AsyncOpenAI
import os

client = AsyncOpenAI()

TOKEN = os.environ.get("BOT_TOKEN", "")
SYSTEM_PROMPT = "Ты - помощник, который помогает пользователю с его вопросами."
MAX_HISTORY = 20
ERROR_MESSAGE = "Не получилось получить ответ от AI. Попробуйте ещё раз чуть позже."

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Чем могу помочь?")


async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if "messages" not in context.user_data:
        context.user_data["messages"] = [{"role": "system", "content": SYSTEM_PROMPT}]
    if not update.message or not update.message.text:
        return
    text = update.message.text
    context.user_data["messages"].append({"role": "user", "content": text})
    system_message = context.user_data["messages"][0]
    history = context.user_data["messages"][1:]
    context.user_data["messages"] = [system_message] + history[-MAX_HISTORY:]
    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.TYPING
    )
    ai_answer = await get_ai_response(context.user_data["messages"])
    if ai_answer == ERROR_MESSAGE:
        if context.user_data["messages"][-1]["role"] == "user":
            context.user_data["messages"].pop()
        await update.message.reply_text(ai_answer)
        return
    context.user_data["messages"].append({
            "role": "assistant", "content": ai_answer
        })
    history = context.user_data["messages"][1:]
    context.user_data["messages"] = [system_message] + history[-MAX_HISTORY:]
    await update.message.reply_text(ai_answer)

async def get_ai_response(messages):
    try:
        response = await client.chat.completions.create( 
            model = "gpt-4o-mini",
            messages=messages,
        )
        ai_answer = response.choices[0].message.content
        print(ai_answer)
        return ai_answer
    except Exception as e:
        print(f"OpenAI error: {e}")
        return ERROR_MESSAGE

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_answer))

    print("Бот запущен...")

    app.run_polling()

if __name__ == "__main__":
    main()