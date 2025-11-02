"""Main module for the stock data pipeline project."""

from rich.console import Console
from dotenv import load_dotenv
import os
from .extract.api_extractor import extract_from_api
from .transform.transform_digital_currency import transform_market_data
from .load.load_to_bigquery import load_to_bigquery 

console = Console()

def main():
    # data = process_digital_currency_daily("BTC", "EUR")
    url = "https://www.alphavantage.co/query"
    function = "DIGITAL_CURRENCY_DAILY"
    symbol = "BTC"
    market = "USD"
    API_KEY = os.getenv("API_KEY_ALPHA")
    api = (
        f"{url}"
        f"?function={function}"
        f"&symbol={symbol}"
        f"&market={market}"
        f"&apikey={API_KEY}"
    )
    # 1. Extract
    # raw_data = extract_from_api(api)

    # 2. Transform
    clean_df = transform_market_data()

    # 3. Load
    project_id = "productos-320620"
    load_to_bigquery(clean_df, "productos-320620.sales_dataset.sales", project_id)


if __name__ == "__main__":
    main()
