

import typing

PlaidErrorType = typing.Union[
    typing.Literal[
        "INVALID_REQUEST",
        "INVALID_RESULT",
        "INVALID_INPUT",
        "INSTITUTION_ERROR",
        "RATE_LIMIT_EXCEEDED",
        "API_ERROR",
        "ITEM_ERROR",
        "ASSET_REPORT_ERROR",
        "RECAPTCHA_ERROR",
        "OAUTH_ERROR",
        "PAYMENT_ERROR",
        "BANK_TRANSFER_ERROR",
        "INCOME_VERIFICATION_ERROR",
        "MICRODEPOSITS_ERROR",
    ],
    typing.Any,
]
