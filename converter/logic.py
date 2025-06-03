from .api import get_fiat_rates, get_crypto_rate

FIAT = ['USD', 'EUR', 'RUB', 'KZT', 'CNY', 'INR', 'VETKA']
HAHA = ['BANAN']
CRYPTO = ['BTC', 'ETH', 'USDT']

def convert_currency(text: str) -> str:
    try:
        amount, from_cur, to_cur = text.upper().split()
        amount = float(amount)
        # VETKA 
        if from_cur in HAHA or to_cur in HAHA:
            return f"{amount} {from_cur} = {amount} {to_cur} (это шутка, братуха!)"
        if from_cur in FIAT and to_cur in FIAT:
            rates = get_fiat_rates(from_cur)
            rate = rates.get(to_cur)
        elif from_cur in CRYPTO and to_cur in FIAT:
            rate = get_crypto_rate(from_cur, to_cur)
        elif from_cur in FIAT and to_cur in CRYPTO:
            # Получаем курс FIAT->USD, затем USD->CRYPTO
            if from_cur != 'USD':
                rates = get_fiat_rates(from_cur)
                usd_rate = rates.get('USD')
                if not usd_rate:
                    return "ошибка получения курса №1."
                amount_in_usd = amount * usd_rate
            else:
                amount_in_usd = amount
            rate = get_crypto_rate('USD', to_cur)
            if rate:
                return f"{amount} {from_cur} = {amount_in_usd / rate:.6f} {to_cur}"
        elif from_cur in CRYPTO and to_cur in CRYPTO:
            # Сначала переводим в USD, потом в нужную крипту
            usd = get_crypto_rate(from_cur, 'USD')
            if not usd:
                return "ошибка получения курса №2."
            rate = get_crypto_rate('USD', to_cur)
            if not rate:
                return "ошибка получения курса №3."
            result = amount * usd / rate
            return f"{amount} {from_cur} = {result:.6f} {to_cur}"
        else:
            return "валюта не поддерживается №5."
        if not rate:
            return "ошибка получения курса №6."
        result = amount * rate
        return f"{amount} {from_cur} = {result:.6f} {to_cur}"
    except Exception:
        return "введите запрос в формате: 100 USD RUB или 100 BTC ETH."
# Если возникла ошибка, возвращаем сообщение об ошибке