import requests

# FIAT_API_URL = "https://api.exchangerate.host/latest"
# CRYPTO_API_URL = "https://min-api.cryptocompare.com/data/price"

# Для теста возвращаем статичные курсы
def get_fiat_rates(base: str):
    # Пример статичных курсов относительно базовой валюты
    static_rates = {
        'USD': {'EUR': 0.92, 'RUB': 89.0, 'KZT': 450.0, 'CNY': 7.2, 'INR': 83.0, 'USD': 1.0},
        'EUR': {'USD': 1.09, 'RUB': 97.0, 'KZT': 490.0, 'CNY': 7.8, 'INR': 90.0, 'EUR': 1.0},
        'RUB': {'USD': 0.011, 'EUR': 0.010, 'KZT': 5.1, 'CNY': 0.081, 'INR': 0.93, 'RUB': 1.0},
        'KZT': {'USD': 0.0022, 'EUR': 0.0020, 'RUB': 0.20, 'CNY': 0.016, 'INR': 0.18, 'KZT': 1.0},
        'VETKA': {'USD': 1.0, 'EUR': 1.0, 'RUB': 1.0, 'KZT': 1.0, 'CNY': 1.0, 'INR': 1.0, 'VETKA': 2.0},
    }
    return static_rates.get(base, {})

def get_crypto_rate(from_symbol: str, to_symbol: str):
    # Пример статичных курсов для криптовалют
    static_crypto = {
        'BTC': {'USD': 65000, 'ETH': 18, 'USDT': 65000, 'BTC': 1.0},
        'ETH': {'USD': 3600, 'BTC': 0.055, 'USDT': 3600, 'ETH': 1.0},
        'USDT': {'USD': 1.0, 'BTC': 0.000015, 'ETH': 0.00028, 'USDT': 1.0},
    }
    rates = static_crypto.get(from_symbol, {})
    return rates.get(to_symbol)

# Для плавающих курсов берем API
# def get_fiat_rates(base: str):
#     response = requests.get(FIAT_API_URL, params={'base': base})
#     data = response.json()
#     return data.get('rates', {})

# def get_crypto_rate(from_symbol: str, to_symbol: str):
#     params = {'fsym': from_symbol, 'tsyms': to_symbol}
#     response = requests.get(CRYPTO_API_URL, params=params)
#     data = response.json()
#     return data.get(to_symbol)