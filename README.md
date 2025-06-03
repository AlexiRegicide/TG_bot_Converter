# Currency & Crypto Converter Telegram Bot

Это Python-проект Telegram-бота для конвертации популярных валют (USD, EUR, RUB, KZT, CNY, INR) и криптовалют (BTC, ETH, USDT). Проект использует библиотеку `telebot` и внешние API для получения актуальных курсов.

## Структура проекта

- `bot.py` — точка входа, запуск Telegram-бота
- `config.py` — настройки: токен Telegram, параметры API
- `requirements.txt` — зависимости проекта
- `converter/`
  - `api.py` — работа с внешними API (валюты и криптовалюты)
  - `logic.py` — бизнес-логика конвертации
- `keyboards/`
  - `keyboards.py` — клавиатуры для Telegram-бота

## Требования

- Python 3.12 или новее
- Библиотека [pyTelegramBotAPI (telebot)](https://pypi.org/project/pyTelegramBotAPI/)
- Библиотека [requests](https://pypi.org/project/requests/)

## Установка

1. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

2. Запустите бота:

   ```bash
   python bot.py
   ```

3. Укажите свой Telegram токен и параметры API в `config.py`.

## Использование

- Отправьте боту сообщение в формате:  
  `100 USD RUB`  
  или  
  `0.01 BTC USD`  
  чтобы получить результат конвертации.

---
