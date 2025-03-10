import json
import time

# Function to save conversion history in a JSON file
# Adds a record with amount, currencies, and timestamp to a file
def save_conversion(amount, base_currency, converted_amount, target_currency):
    record = {
        "amount": amount,
        "base_currency": base_currency,
        "converted_amount": converted_amount,
        "target_currency": target_currency,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    with open("conversion_history.json", "a") as file:
        json.dump(record, file)
        file.write("\n")