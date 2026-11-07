

import typing

OauthScope = typing.Union[
    typing.Literal[
        "payments",
        "checkouts.read",
        "checkouts.write",
        "transactions.history",
        "transactions.read",
        "refunds.write",
        "receipts.read",
        "user.profile_readonly",
        "user.profile",
        "user.app-settings",
        "payment_instruments",
        "customers.read",
        "customers.write",
        "user.payout-settings",
        "payouts.read",
        "user.subaccounts",
    ],
    typing.Any,
]
