

import typing

CreditUnofficialCurrencyCode = typing.Optional[str]
"""
The unofficial currency code associated with the amount or balance. Always `null` if `iso_currency_code` is non-null.
Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.
"""
