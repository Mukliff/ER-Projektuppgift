from exchange_rate import get_exchange_rate
from history import save_conversion

# Function to convert currency
# Takes the amount, base currency, and target currency, fetches the exchange rate, and calculates the converted amount
# Saves the conversion in a file and returns the converted amount
def convert_currency(amount, base_currency, target_currency):
    rate = get_exchange_rate(base_currency, target_currency)
    if rate:
        converted_amount = amount * rate
        save_conversion(amount, base_currency, converted_amount, target_currency)
        return converted_amount
    else:
        return None