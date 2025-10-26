"""Main module for the stock data pipeline project."""

from rich.console import Console
from .api.controllers.cripto_currencies import process_currency_exchange_rate, process_digital_currency_daily

console = Console()

def main():
    data = process_digital_currency_daily("BTC", "EUR")
    console.print(data)


if __name__ == "__main__":
    main()
