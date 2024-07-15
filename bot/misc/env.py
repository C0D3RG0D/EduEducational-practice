from os import environ
from typing import Final


class TgKeys:
    TOKEN: Final = environ.get('TG_TOKEN', 'define me!')
    PAYMENT_TOKEN: Final = environ.get('PAYMENT_TOKEN', 'define me!')
