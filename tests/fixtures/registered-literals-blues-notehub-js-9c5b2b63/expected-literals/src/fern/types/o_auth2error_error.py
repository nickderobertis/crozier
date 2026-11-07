

import typing

OAuth2ErrorError = typing.Union[
    typing.Literal[
        "invalid_request",
        "invalid_client",
        "invalid_grant",
        "unauthorized_client",
        "unsupported_grant_type",
        "invalid_scope",
    ],
    typing.Any,
]
