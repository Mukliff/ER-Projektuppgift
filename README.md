# Currency Converter

A Python program that fetches real-time exchange rates and performs currency conversions. The program also stores a history of conversions and automatically updates exchange rates every hour.

## 📦 Features

- Fetch real-time exchange rates from an online API.
- Convert amounts between different currencies.
- Automatically update and store exchange rates every hour.
- Save all conversions in a history file (`conversion_history.json`).

## 📂 Project Structure

```
currency_converter/
│
├── main.py                  # Main program (user interface and interaction)
├── exchange_rate.py         # Fetches exchange rates from API
├── converter.py             # Handles currency conversion logic
├── history.py               # Handles saving conversion history to a file
└── scheduler.py             # Handles automatic updates of exchange rates
```

## ⚙️ How It Works

### Currency Conversion

- The user is prompted to enter:
  - Base currency (e.g., USD)
  - Target currency (e.g., EUR)
  - Amount to convert
- The program fetches the latest exchange rate and performs the conversion.
- The conversion and rate are saved in `conversion_history.json`.

### Automatic Exchange Rate Updates

- Every hour, the program automatically fetches the exchange rate from **USD** to **EUR** and saves it to the history file.

## 💾 Conversion History

All conversions are stored in a file called `conversion_history.json` with this format:
```json
{
  "amount": 100,
  "base_currency": "USD",
  "converted_amount": 91.23,
  "target_currency": "EUR",
  "timestamp": "2025-03-10 12:34:56"
}
```

## 🚀 How to Run

1. Make sure you have **Python 3.x** installed.

2. Install required packages (if not already installed):
```bash
pip install requests schedule
```

3. Run the main program:
```bash
python main.py
```

4. Follow the prompts to perform a currency conversion.

> **Note:** The automatic update runs in the background and does not block the program.

## 🔑 Requirements

- Python 3.x
- `requests` library
- `schedule` library

## 🌐 API

- The program uses [ExchangeRate-API](https://www.exchangerate-api.com/) for fetching exchange rates.
