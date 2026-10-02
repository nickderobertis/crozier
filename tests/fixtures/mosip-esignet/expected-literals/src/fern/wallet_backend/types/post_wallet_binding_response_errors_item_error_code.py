

import typing

PostWalletBindingResponseErrorsItemErrorCode = typing.Union[
    typing.Literal[
        "key_binding_failed",
        "invalid_public_key",
        "invalid_auth_challenge",
        "duplicate_public_key",
        "invalid_auth_factor_type_format",
        "invalid_auth_factor_type",
        "invalid_challenge",
        "invalid_challenge_length",
        "invalid_challenge_format",
    ],
    typing.Any,
]
