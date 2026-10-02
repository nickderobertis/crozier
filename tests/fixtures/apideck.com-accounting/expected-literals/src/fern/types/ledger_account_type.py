

import typing

LedgerAccountType = typing.Union[
    typing.Literal[
        "accounts_receivable",
        "revenue",
        "sales",
        "other_income",
        "bank",
        "current_asset",
        "fixed_asset",
        "non_current_asset",
        "other_asset",
        "balancesheet",
        "equity",
        "expense",
        "other_expense",
        "costs_of_sales",
        "accounts_payable",
        "credit_card",
        "current_liability",
        "non_current_liability",
        "other_liability",
    ],
    typing.Any,
]
