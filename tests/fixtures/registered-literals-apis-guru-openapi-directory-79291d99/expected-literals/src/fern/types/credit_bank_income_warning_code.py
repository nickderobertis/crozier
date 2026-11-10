

import typing

CreditBankIncomeWarningCode = typing.Union[
    typing.Literal[
        "IDENTITY_UNAVAILABLE", "TRANSACTIONS_UNAVAILABLE", "ITEM_UNAPPROVED", "REPORT_DELETED", "DATA_UNAVAILABLE"
    ],
    typing.Any,
]
