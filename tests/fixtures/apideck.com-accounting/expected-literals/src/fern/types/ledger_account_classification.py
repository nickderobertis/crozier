

import typing

LedgerAccountClassification = typing.Union[
    typing.Literal[
        "asset",
        "equity",
        "expense",
        "liability",
        "revenue",
        "income",
        "other_income",
        "other_expense",
        "costs_of_sales",
    ],
    typing.Any,
]
