

import typing

TransactionCode = typing.Union[
    typing.Literal[
        "adjustment",
        "atm",
        "bank charge",
        "bill payment",
        "cash",
        "cashback",
        "cheque",
        "direct debit",
        "interest",
        "purchase",
        "standing order",
        "transfer",
    ],
    typing.Any,
]
