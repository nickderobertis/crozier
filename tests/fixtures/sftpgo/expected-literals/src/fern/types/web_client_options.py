

import typing

WebClientOptions = typing.Union[
    typing.Literal[
        "publickey-change-disabled",
        "tls-cert-change-disabled",
        "write-disabled",
        "mfa-disabled",
        "password-change-disabled",
        "api-key-auth-change-disabled",
        "info-change-disabled",
        "shares-disabled",
        "password-reset-disabled",
        "shares-without-password-disabled",
    ],
    typing.Any,
]
