import telebot
from config import TELEGRAM_TOKEN
from converter.logic import convert_currency
from keyboards.keyboards import get_main_keyboard

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(content_types=['text'])
def handle_message(message):
    text = message.text

    #обработка команд
    if text == 'Старт' or text == '/start':
        bot.send_message(
            message.chat.id,
            "Привет! Ты получил зарплату веткой? Могу помочь с конвертацией валют: USD, EUR, RUB, KZT, ETH, BTC. Какой курс тебя интересует?\n"
            "Выберите действие или введите сумму и валюту для конвертации.",
            reply_markup=get_main_keyboard()
        )
    elif text == 'Помощь':
        bot.send_message(
            message.chat.id,
            "Список доступных валют: \n"
            "USD, EUR, RUB, KZT, ETH, BTC, VETKA.\n"
            "Просто введи сумму и валюту в формате: 100 VETKA USD."
        )
    elif text == 'Курс валют':
        bot.send_message(
            message.chat.id,
            "Потом доделаю курс валют, пока только конвертация."
        )
    elif text == 'Конвертировать':
        bot.send_message(
            message.chat.id,
            "Введите сумму и валюты в формате: 100 VETKA USD.\n"
            "Информацию о доступных валютах можно получить в разделе 'Помощь'.\n"
        )
    elif text == 'Назад':
        bot.send_message(
            message.chat.id,
            "Окей.\n Выберите действие из меню:", 
            reply_markup=get_main_keyboard()
        )
    elif text == 'Главная':
        bot.send_message(
            message.chat.id,
            "Вы можете выбрать одно из следующих действий: \n"
            "Старт, Помощь, Курс валют, Конвертировать, Назад, О боте, О разработчике, Стоп, Выход.",
            reply_markup=get_main_keyboard()
        )
    elif text == 'О боте':
        bot.send_message(
            message.chat.id,
            "Этот бот создан для конвертации валют, веток, а также получения курса валют.\n"
        )
    elif text == 'О разработчике':
        bot.send_message(
            message.chat.id,
            "Разработчик: @usagi_regicide. Если у вас есть вопросы или предложения, пишите мне!"
        )
    elif text == 'Выход':
        bot.send_message(
            message.chat.id,
            "Всего хорошего!",
            reply_markup=get_main_keyboard()
        )
    # обработка конвертации валют
    elif ' ' in message.text:
        result = convert_currency(message.text)
        bot.send_message(message.chat.id, result, reply_markup=get_main_keyboard())

if __name__ == '__main__':
    bot.polling(none_stop=True)

