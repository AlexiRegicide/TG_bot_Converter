from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_keyboard():
    buttons = [
        [KeyboardButton('USD'), KeyboardButton('EUR'), KeyboardButton('RUB')],
        [KeyboardButton('KZT'), KeyboardButton('CNY'), KeyboardButton('INR')],
        [KeyboardButton('BTC'), KeyboardButton('ETH'), KeyboardButton('USDT')],
        [KeyboardButton('BANAN'), KeyboardButton('VETKA')]
    ]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for row in buttons:
        markup.add(*row)
    return markup