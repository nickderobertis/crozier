

import typing

PostAuthenticateV3ResponseErrorsItemErrorCode = typing.Union[
    typing.Literal[
        "invalid_transaction",
        "invalid_identifier",
        "invalid_no_of_challenges",
        "auth_failed",
        "unknown_error",
        "invalid_auth_factor_type_format",
        "invalid_auth_factor_type",
        "invalid_challenge",
        "invalid_challenge_length",
        "invalid_challenge_format",
        "invalid_captcha",
    ],
    typing.Any,
]
