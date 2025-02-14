import requests
import json
import time
import schedule
import threading

# Funktion för att hämta valutakurser från API
# Tar in en basvaluta och en målvaluta och hämtar växelkursen från API:et
# Returnerar växelkursen om den hittas, annars None
def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['rates'].get(target_currency, None)
    except requests.RequestException as e:
        print(f"Fel vid hämtning av valutakurser: {e}")
        return None

# Funktion för att konvertera valuta
# Tar in beloppet, basvalutan och målvalutan, hämtar växelkursen och beräknar det konverterade beloppet
# Sparar konverteringen i en fil och returnerar det konverterade beloppet
def convert_currency(amount, base_currency, target_currency):
    rate = get_exchange_rate(base_currency, target_currency)
    if rate:
        converted_amount = amount * rate
        save_conversion(amount, base_currency, converted_amount, target_currency)
        return converted_amount
    else:
        return None

# Funktion för att spara konverteringshistorik i en JSON-fil
# Lägger till en post med belopp, valutor och tidsstämpel i en fil
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

# Automatiserad funktion för att hämta och spara aktuella valutakurser varje timme
# Hämtar valutakurs mellan USD och EUR och sparar den i historiken
def automated_currency_update():
    print("Hämtar automatiska valutakurser...")
    base_currency = "USD"
    target_currency = "EUR"
    rate = get_exchange_rate(base_currency, target_currency)
    if rate:
        save_conversion(1, base_currency, rate, target_currency)
        print(f"Sparade uppdaterad valutakurs: 1 {base_currency} = {rate:.2f} {target_currency}")
    else:
        print("Misslyckades med att uppdatera valutakurser.")

# Schemalägg automatiseringen att köras varje timme
schedule.every(1).hours.do(automated_currency_update)

# Kör schemaläggaren i en separat tråd för att inte blockera programmet
# Denna funktion körs i en loop som ständigt kollar om schemalagda uppgifter ska köras
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Startar schemaläggaren i en bakgrundstråd
threading.Thread(target=run_scheduler, daemon=True).start()

# Huvudprogrammet som låter användaren ange valutor och belopp för konvertering
if __name__ == "__main__":
    base_currency = input("Ange basvaluta (t.ex. USD): ").upper()
    target_currency = input("Ange målvaluta (t.ex. EUR): ").upper()
    try:
        amount = float(input("Ange belopp: "))
        converted_amount = convert_currency(amount, base_currency, target_currency)
        if converted_amount:
            print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
        else:
            print("Kunde inte hämta valutakursen.")
    except ValueError:
        print("Ogiltigt belopp.")
