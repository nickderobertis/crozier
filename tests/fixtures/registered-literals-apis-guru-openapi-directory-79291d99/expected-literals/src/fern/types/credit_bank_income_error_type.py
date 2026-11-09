

import typing

CreditBankIncomeErrorType = typing.Union[
    typing.Literal[
        "INTERNAL_SERVER_ERROR",
        "INSUFFICIENT_CREDENTIALS",
        "ITEM_LOCKED",
        "USER_SETUP_REQUIRED",
        "COUNTRY_NOT_SUPPORTED",
        "INSTITUTION_DOWN",
        "INSTITUTION_NO_LONGER_SUPPORTED",
        "INSTITUTION_NOT_RESPONDING",
        "INVALID_CREDENTIALS",
        "INVALID_MFA",
        "INVALID_SEND_METHOD",
        "ITEM_LOGIN_REQUIRED",
        "MFA_NOT_SUPPORTED",
        "NO_ACCOUNTS",
        "ITEM_NOT_SUPPORTED",
        "ACCESS_NOT_GRANTED",
    ],
    typing.Any,
]
