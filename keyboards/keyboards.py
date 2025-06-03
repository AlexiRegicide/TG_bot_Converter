from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Кастомные кнопки для клавиатуры ИНЛАЙН
def get_main_inline_keyboard():
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("Помощь", callback_data="help"),
        types.InlineKeyboardButton("Курс валют", callback_data="rates"),
    )
    markup.add(
        types.InlineKeyboardButton("Конвертировать", callback_data="convert"),
        types.InlineKeyboardButton("О боте", callback_data="about_bot"),
    )
    markup.add(
        types.InlineKeyboardButton("О разработчике", callback_data="about_dev"),
        types.InlineKeyboardButton("Выход", callback_data="exit"),
    )
    return markup









# Кастомные кнопки для клавиатуры ТЕКСТ
# def get_main_keyboard():
#     buttons = [
#         [KeyboardButton('Старт'), KeyboardButton('Помощь')],
#         [KeyboardButton('Курс валют'), KeyboardButton('Конвертировать')],
# #        [KeyboardButton('Выход'), KeyboardButton('Отмена')], ДОДЕЛАТЬ, КОГДА БУДЕТ КУРС ВАЛЮТ
#         [KeyboardButton('О боте'), KeyboardButton('О разработчике')]
# #       [KeyboardButton('Назад'), KeyboardButton('Главная')],    ДОДЕЛАТЬ, КОГДА БУДЕТ КУРС ВАЛЮТ 
#     ]
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     for row in buttons:
#         markup.add(*row)

#     return markup