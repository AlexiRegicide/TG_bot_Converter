import telebot
from config import TELEGRAM_TOKEN
from converter.logic import convert_currency
from keyboards.keyboards import get_main_inline_keyboard
# from keyboards.keyboards import get_main_keyboard ДЛЯ ТЕКСТОВЫХ КНОПОК

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(content_types=['text'])
def handle_message(message):
    text = message.text
    if text == 'Старт' or text == '/start':
        bot.send_message(
            message.chat.id,
            "Привет! Ты получил зарплату веткой?\n"
            "Этот бот поможет тебе конвертировать ветки в другие валюты и своевременно узнавать курс.\n"
            "Могу помочь с конвертацией валют: USD, EUR, RUB, KZT, ETH, BTC.\n"
            "Выберите действие в меню или введите сумму и валюту для конвертации.",
            reply_markup=get_main_inline_keyboard()
        )
    elif ' ' in message.text:
        result = convert_currency(message.text)
        bot.send_message(message.chat.id, result, reply_markup=get_main_inline_keyboard())

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "help":
        bot.send_message(
            call.message.chat.id,
            "Список доступных валют: \n"
            "USD, EUR, RUB, KZT, ETH, BTC, VETKA.\n"
            "Просто введи сумму и валюту в формате: 100 VETKA USD.\n"
            "Информацию о разработчике и боте можно получить в соответствующих разделах.\n",
            reply_markup=get_main_inline_keyboard()
        )
    elif call.data == "rates":
        bot.send_message(
            call.message.chat.id,
            "Потом доделаю курс валют, пока только конвертация.",
            reply_markup=get_main_inline_keyboard()
        )
    elif call.data == "convert":
        bot.send_message(
            call.message.chat.id,
            "Введите сумму и валюты в формате: 100 VETKA USD.\n"
            "Информацию о доступных валютах можно получить в разделе 'Помощь'.\n",
            reply_markup=get_main_inline_keyboard()
        )
    elif call.data == "about_bot":
        bot.send_message(
            call.message.chat.id,
            "Этот бот создан для конвертации валют, веток, а также получения курса валют.\n",
            reply_markup=get_main_inline_keyboard()
        )
    elif call.data == "about_dev":
        bot.send_message(
            call.message.chat.id,
            "Разработчик: @usagi_regicide. Если у вас есть вопросы или предложения, пишите мне!",
            reply_markup=get_main_inline_keyboard()
        )
    elif call.data == "exit":
        bot.send_message(
            call.message.chat.id,
            "Всего хорошего!",
            reply_markup=get_main_inline_keyboard()
        )
    bot.answer_callback_query(call.id)

if __name__ == '__main__':
    bot.polling(none_stop=True)





# Текстовые кнопки для клавиатуры
# @bot.message_handler(content_types=['text'])
# def handle_message(message):
#     text = message.text
#     #обработка команд
#     if text == 'Старт' or text == '/start':
#         bot.send_message(
#             message.chat.id,
#             "Привет! Ты получил зарплату веткой?\n"
#             "Этот бот поможет тебе конвертировать ветки в другие валюты и своевременно узнавать курс.\n"
#             "Могу помочь с конвертацией валют: USD, EUR, RUB, KZT, ETH, BTC.\n"
#             "Выберите действие в меню или введите сумму и валюту для конвертации.",
#             reply_markup=get_main_keyboard()
#         )
#     elif text == 'Помощь':
#         bot.send_message(
#             message.chat.id,
#             "Список доступных валют: \n"
#             "USD, EUR, RUB, KZT, ETH, BTC, VETKA.\n"
#             "Просто введи сумму и валюту в формате: 100 VETKA USD.\n"
#             "Информацию о разработчике и боте можно получить в соответствующих разделах.\n"
#         )
#     elif text == 'Курс валют':
#         bot.send_message(
#             message.chat.id,
#             "Потом доделаю курс валют, пока только конвертация."
#         )
#     elif text == 'Конвертировать':
#         bot.send_message(
#             message.chat.id,
#             "Введите сумму и валюты в формате: 100 VETKA USD.\n"
#             "Информацию о доступных валютах можно получить в разделе 'Помощь'.\n"
#         )
#     elif text == 'О боте':
#         bot.send_message(
#             message.chat.id,
#             "Этот бот создан для конвертации валют, веток, а также получения курса валют.\n"
#         )
#     elif text == 'О разработчике':
#         bot.send_message(
#             message.chat.id,
#             "Разработчик: @usagi_regicide. Если у вас есть вопросы или предложения, пишите мне!"
#         )
#     elif text == 'Выход':
#         bot.send_message(
#             message.chat.id,
#             "Всего хорошего!",
#             reply_markup=get_main_keyboard()
#         )
#     # обработка конвертации валют
#     elif ' ' in message.text:
#         result = convert_currency(message.text)
#         bot.send_message(message.chat.id, result, reply_markup=get_main_keyboard())


