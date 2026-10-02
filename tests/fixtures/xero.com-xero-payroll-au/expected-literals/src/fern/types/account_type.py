

import typing

AccountType = typing.Union[
    typing.Literal[
        "BANK",
        "CURRENT",
        "CURRLIAB",
        "DEPRECIATN",
        "DIRECTCOSTS",
        "EQUITY",
        "EXPENSE",
        "FIXED",
        "INVENTORY",
        "LIABILITY",
        "NONCURRENT",
        "OTHERINCOME",
        "OVERHEADS",
        "PREPAYMENT",
        "REVENUE",
        "SALES",
        "TERMLIAB",
        "PAYGLIABILITY",
        "PAYG",
        "SUPERANNUATIONEXPENSE",
        "SUPERANNUATIONLIABILITY",
        "WAGESEXPENSE",
        "WAGESPAYABLELIABILITY",
    ],
    typing.Any,
]
