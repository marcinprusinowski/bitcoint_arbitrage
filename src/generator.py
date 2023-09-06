import random


def generate_currencies(num_currencies):
    return [f"CUR{i + 1}" for i in range(num_currencies)]


def generate_rates(currencies):
    rates = {}
    for base_currency in currencies:
        for quote_currency in currencies:
            if base_currency == quote_currency:
                rate = "1.00000000"
            else:
                random_rate = random.uniform(0.01, 100)
                rate = f"{random_rate:.8f}"
            rates[f"{base_currency}-{quote_currency}"] = rate
    return rates
