from config import BOT_TOKEN
from handlers import start, handle_answer, clear, history, time_command, stats
from telegram.ext import (Application, CommandHandler, MessageHandler, filters)
from database import create_messages_table



def main():
    create_messages_table()
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("clear", clear))
    app.add_handler(CommandHandler("history", history))
    app.add_handler(CommandHandler("time", time_command))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_answer))
    
    print("Бот запущен...")

    app.run_polling()


if __name__ == "__main__":
    main()