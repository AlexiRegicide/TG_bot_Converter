import telebot
from config import TELEGRAM_TOKEN
from converter.logic import convert_currency
from keyboards.keyboards import get_main_keyboard

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['/темка'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "Здарова, братуха! Темка новая? Смотри, могу помочь с конвертацией валют: USD, EUR, RUB, KZT, ETH, BTC.\n"
        "Формат твоего запроса: 100 USD RUB",
        reply_markup=get_main_keyboard()
    )

@bot.message_handler(func=lambda m: m.text == 'отключайся епть-тудэй')
def shutdown(message):
    bot.send_message(message.chat.id, "Понял, братуха. Выключаюсь. Если что, пиши!")

@bot.message_handler(content_types=['text'])
def handle_message(message):
    if message.text == 'отключайся епть-тудэй':
        shutdown(message)
        return
    result = convert_currency(message.text)
    bot.send_message(message.chat.id, result, reply_markup=get_main_keyboard())

if __name__ == '__main__':
    bot.polling(none_stop=True)

# This code initializes a Telegram bot that can convert currencies based on user input.