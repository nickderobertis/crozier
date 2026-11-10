

import typing

CreditBankIncomeCategory = typing.Union[
    typing.Literal[
        "SALARY",
        "UNEMPLOYMENT",
        "CASH",
        "GIG_ECONOMY",
        "RENTAL",
        "CHILD_SUPPORT",
        "MILITARY",
        "RETIREMENT",
        "LONG_TERM_DISABILITY",
        "BANK_INTEREST",
        "CASH_DEPOSIT",
        "TRANSFER_FROM_APPLICATION",
        "TAX_REFUND",
        "OTHER",
    ],
    typing.Any,
]
