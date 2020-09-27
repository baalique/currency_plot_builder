from dataclasses import dataclass
from datetime import date

import requests


@dataclass
class CurrencyPair:
    currency_x: str
    currency_y: str


class Currency:
    def __init__(self, currencies: CurrencyPair):
        self.currencies = currencies

    def __str__(self):
        return f'{self.currencies.currency_x} -> {self.currencies.currency_y}'

    def get_rate(self, start_date: date, stop_date: date) -> dict:
        exchange_url = 'https://api.exchangeratesapi.io/'
        url = f'{exchange_url}history?start_at={start_date}&end_at={stop_date}&' \
              f'base={self.currencies.currency_x}&symbols={self.currencies.currency_y}'
        response = requests.get(url)
        return response.json()
