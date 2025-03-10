import time
import schedule
import threading
from exchange_rate import get_exchange_rate
from history import save_conversion

# Automated function to fetch and save current exchange rates every hour
# Fetches the exchange rate between USD and EUR and saves it in the history
def automated_currency_update():
    print("Fetching automatic exchange rates...")
    base_currency = "USD"
    target_currency = "EUR"
    rate = get_exchange_rate(base_currency, target_currency)
    if rate:
        save_conversion(1, base_currency, rate, target_currency)
        print(f"Saved updated exchange rate: 1 {base_currency} = {rate:.2f} {target_currency}")
    else:
        print("Failed to update exchange rates.")

# Schedule the automation to run every hour
schedule.every(1).hours.do(automated_currency_update)

# Run the scheduler in a separate thread so it doesn't block the program
# This function runs in a loop constantly checking if scheduled tasks should run
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Starts the scheduler in a background thread
threading.Thread(target=run_scheduler, daemon=True).start()