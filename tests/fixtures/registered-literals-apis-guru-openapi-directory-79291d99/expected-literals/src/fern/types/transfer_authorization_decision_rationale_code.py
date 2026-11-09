

import typing

TransferAuthorizationDecisionRationaleCode = typing.Union[
    typing.Literal[
        "NSF",
        "RISK",
        "TRANSFER_LIMIT_REACHED",
        "MANUALLY_VERIFIED_ITEM",
        "ITEM_LOGIN_REQUIRED",
        "PAYMENT_PROFILE_LOGIN_REQUIRED",
        "ERROR",
        "MIGRATED_ACCOUNT_ITEM",
    ],
    typing.Any,
]
