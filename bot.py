import telebot
from config import TELEGRAM_TOKEN
from converter.logic import convert_currency
from keyboards.keyboards import get_main_keyboard

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# @bot.message_handler(commands=['/темка'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "Привет! Ты получил зарплату не веткой? Могу помочь с конвертацией валют: USD, EUR, RUB, KZT, ETH, BTC. Какой курс тебя интересует?",
        reply_markup=get_main_keyboard()
    )

# @bot.message_handler(commands=['start'])
# def start_command(message):
#     bot.send_message(
#         message.chat.id,
#         "Формат ввода данных **100 VETKA USD**.",
#         reply_markup=get_main_keyboard()
#     )

# @bot.message_handler(func=lambda m: m.text == 'stop')
# def shutdown(message):
#     bot.send_message(message.chat.id, "Всего хорошего, возвращайся с новыми страданиями!")

@bot.message_handler(content_types=['text'])
def handle_message(message):
    text = message.text

    #обработка команд
    if text == 'Старт':
        bot.send_message(
            message.chat.id,
            "Выберите действие или введите сумму и валюту для конвертации.",
            reply_markup=get_main_keyboard()
        )
    elif text == 'Помощь':
        bot.send_message(
            message.chat.id,
            "Я могу помочь с конвертацией валют. Просто введи сумму и валюту в формате: **100 VETKA USD**."
        )
    elif text == 'Курс валют':
        bot.send_message(
            message.chat.id,
            "потом доделаю курс валют, пока только конвертация",
        )
    elif text == 'Конвертировать':
        bot.send_message(
            message.chat.id,
            "Введите сумму и валюты в формате: **100 VETKA USD**."
        )
    elif text == 'Назад':
        bot.send_message(
            message.chat.id,
            "Выберите действие:", 
            reply_markup=get_main_keyboard()
        )
    elif text == 'Главная':
        bot.send_message(
            message.chat.id,
            "Вы можете выбрать одно из следующих действий: \n",
            "Старт, Помощь, Курс валют, Конвертировать, Назад, О боте, О разработчике, Стоп, Выход.",
            reply_markup=get_main_keyboard()
        )
    elif text == 'О боте':
        bot.send_message(
            message.chat.id,
            "Этот бот создан для конвертации валют. Просто введите сумму и валюту в формате: **100 VETKA USD**."
        )
    elif text == 'О разработчике':
        bot.send_message(
            message.chat.id,
            "Разработчик: @usagi_regicide. Если у вас есть вопросы или предложения, пишите мне!"
        )
    elif text == 'Стоп' or text == 'Выход':
        bot.send_message(
            message.chat.id,
            "Всего хорошего!",
            reply_markup=get_main_keyboard()
        )

    # обработка конвертации валют
    result = convert_currency(message.text)
    bot.send_message(message.chat.id, result, reply_markup=get_main_keyboard())

if __name__ == '__main__':
    bot.polling(none_stop=True)

