

import typing

PaymentType = typing.Union[
    typing.Literal[
        "CASH", "POS", "ECOM", "RECURRING", "BITCOIN", "BALANCE", "MOTO", "BOLETO", "DIRECT_DEBIT", "APM", "UNKNOWN"
    ],
    typing.Any,
]
