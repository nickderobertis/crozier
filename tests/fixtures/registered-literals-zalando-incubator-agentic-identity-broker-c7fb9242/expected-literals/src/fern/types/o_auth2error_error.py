

import typing

OAuth2ErrorError = typing.Union[
    typing.Literal[
        "invalid_request", "invalid_client", "invalid_grant", "invalid_target", "access_denied", "server_error"
    ],
    typing.Any,
]
