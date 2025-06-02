from telegram import ReplyKeyboardMarkup

def get_main_keyboard():
    buttons = [['USD', 'EUR', 'RUB'], ['KZT', 'CNY', 'INR']]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)