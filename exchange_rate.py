import requests

# Function to fetch exchange rates from API
# Takes a base currency and a target currency and retrieves the exchange rate from the API
# Returns the exchange rate if found, otherwise None
def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['rates'].get(target_currency, None)
    except requests.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return None