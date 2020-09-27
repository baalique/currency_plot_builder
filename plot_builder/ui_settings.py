from datetime import date

_default_x = 200
_default_y = 200
_default_width = 720
_default_height = 480
DEFAULT_GEOMETRY = _default_x, _default_y, _default_width, _default_height
DEFAULT_WINDOWTITLE = 'Currency plot builder'
DEFAULT_START_DATE = date(2020, 1, 1)
DEFAULT_STOP_DATE = date(2020, 1, 10)
DEFAULT_BASE_CURRENCY = 'USD'
DEFAULT_CONVERT_CURRENCY = 'RUB'

CURRENCIES = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS',
              'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB',
              'TRY', 'USD', 'ZAR']
