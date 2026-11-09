

import typing

Products = typing.Union[
    typing.Literal[
        "assets",
        "auth",
        "balance",
        "identity",
        "investments",
        "liabilities",
        "payment_initiation",
        "identity_verification",
        "transactions",
        "credit_details",
        "income",
        "income_verification",
        "deposit_switch",
        "standing_orders",
        "transfer",
        "employment",
        "recurring_transactions",
        "signal",
    ],
    typing.Any,
]
