from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_keyboard():
    buttons = [
        [KeyboardButton('Старт'), KeyboardButton('Помощь')],
        [KeyboardButton('Курс валют'), KeyboardButton('Конвертировать')],
        [KeyboardButton('USD'), KeyboardButton('EUR'), KeyboardButton('RUB')],
        [KeyboardButton('BTC'), KeyboardButton('ETH')],
        [KeyboardButton('Назад'), KeyboardButton('Главная'), KeyboardButton('Отмена')],
        [KeyboardButton('О боте'), KeyboardButton('О разработчике'),]
        [KeyboardButton('Стоп'), KeyboardButton('Выход')]
    ]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for row in buttons:
        markup.add(*row)

    return markup