import requests
import os
from pathlib import Path
from dotenv import load_dotenv
import pandas as pd

env_path = Path(__file__).resolve().parents[1] / "config" / ".env"
load_dotenv(dotenv_path=env_path)
API_KEY = os.getenv("API_KEY_ALPHA")

def get_exchange_rate(from_currency, to_currency):
    function = "CURRENCY_EXCHANGE_RATE"
    if not API_KEY:
        raise ValueError("API_KEY_ALPHA not found in environment variables.")
    url = (
        "https://www.alphavantage.co/query"
        f"?function={function}"
        f"&from_currency={from_currency}"
        f"&to_currency={to_currency}"
        f"&apikey={API_KEY}"
    )
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

def get_digital_currency_daily(symbol, market):
    function = "DIGITAL_CURRENCY_DAILY"
    if not API_KEY:
        raise ValueError("API_KEY_ALPHA not found in environment variables.")
    url = (
        "https://www.alphavantage.co/query"
        f"?function={function}"
        f"&symbol={symbol}"
        f"&market={market}"
        f"&apikey={API_KEY}"
    )
    try: 
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("⏳ Request timed out.")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Request failed: {e}")
    return {}