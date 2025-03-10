from converter import convert_currency
import scheduler  # Ensure the scheduler starts

# The main program that lets the user enter currencies and amounts for conversion
if __name__ == "__main__":
    base_currency = input("Enter base currency (e.g., USD): ").upper()
    target_currency = input("Enter target currency (e.g., EUR): ").upper()
    try:
        amount = float(input("Enter amount: "))
        converted_amount = convert_currency(amount, base_currency, target_currency)
        if converted_amount:
            print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
        else:
            print("Could not fetch the exchange rate.")
    except ValueError:
        print("Invalid amount.")