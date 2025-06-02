from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from keyboards.keyboards import get_main_keyboard
from converter.logic import convert_currency

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я конвертирую валюты: USD, EUR, RUB, KZT, CNY, INR.\n"
        "Введите запрос в формате: 100 USD RUB",
        reply_markup=get_main_keyboard()
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    result = convert_currency(text)
    await update.message.reply_text(result)

def main():
    from config import TELEGRAM_TOKEN
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()

# This code initializes a Telegram bot that can convert currencies based on user input.