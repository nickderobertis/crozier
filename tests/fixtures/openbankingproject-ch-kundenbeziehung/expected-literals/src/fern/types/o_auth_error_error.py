

import typing

OAuthErrorError = typing.Union[
    typing.Literal[
        "invalid_request",
        "invalid_client",
        "invalid_grant",
        "unauthorized_client",
        "unsupported_grant_type",
        "invalid_scope",
        "server_error",
        "temporarily_unavailable",
    ],
    typing.Any,
]
