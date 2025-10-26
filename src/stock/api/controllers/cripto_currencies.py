from ..services.alphavantage import get_exchange_rate, get_digital_currency_daily
import pandas as pd
import re


def process_currency_exchange_rate(from_currency="BTC", to_currency="USD"):
    """Fetches and returns the exchange rate data for the specified cryptocurrencies.

    Returns the raw JSON response from the AlphaVantage service.
    """
    return get_exchange_rate(from_currency, to_currency)


def process_digital_currency_daily(from_currency="BTC", to_currency="USD"):
    digital_currency_daily = get_digital_currency_daily(from_currency, to_currency)
    df = pd.DataFrame(digital_currency_daily)

    return df.head()