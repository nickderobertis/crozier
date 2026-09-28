

import typing

CurrencyRate = typing.Optional[float]
"""
Rate to convert the total amount of the payment into the base currency for the company at the time of the payment.

Currency rates in Codat are implemented as the multiple of foreign currency units to each base currency unit.  

Where the currency rate is provided by the underlying accounting platform, it will be available from Codat with the same precision (up to a maximum of 9 decimal places). 

For accounting platforms which do not provide an explicit currency rate, it is calculated as `baseCurrency / foreignCurrency` and will be returned to 9 decimal places.

## Examples with base currency of GBP

| Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (GBP) |
| :--------------- | :------------- | :------------ | :------------------------- |
| **USD**          | $20            | 0.781         | £15.62                     |
| **EUR**          | €20            | 0.885         | £17.70                     |
| **RUB**          | ₽20            | 0.011         | £0.22                      |

## Examples with base currency of USD

| Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (USD) |
| :--------------- | :------------- | :------------ | :------------------------- |
| **GBP**          | £20            | 1.277         | $25.54                     |
| **EUR**          | €20            | 1.134         | $22.68                     |
| **RUB**          | ₽20            | 0.015         | $0.30                      |
"""
