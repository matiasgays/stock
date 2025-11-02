from ..extract.api_alphavantage import get_exchange_rate, get_digital_currency_daily
import pandas as pd

def process_currency_exchange_rate(from_currency="BTC", to_currency="USD"):
    """Fetches and returns the exchange rate data for the specified cryptocurrencies.

    Returns the raw JSON response from the AlphaVantage service.
    """
    return get_exchange_rate(from_currency, to_currency)


def process_digital_currency_daily(from_currency="BTC", to_currency="USD"):
    df_raw = get_digital_currency_daily(from_currency, to_currency)
    # Basic cleaning
    # df["timestamp"] = pd.to_datetime(df["timestamp"])
    # df = df.sort_values("timestamp")
    # df[["open", "high", "low", "close", "volume"]] = df[["open", "high", "low", "close", "volume"]].astype(float)

    return df_raw

