

import typing

OAuth2ErrorResponseError = typing.Union[
    typing.Literal[
        "invalid_request",
        "invalid_redirect_uri",
        "unauthorized_client",
        "access_denied",
        "unsupported_response_type",
        "invalid_scope",
        "server_error",
        "temporarily_unavailable",
        "invalid_client",
        "invalid_grant",
        "unsupported_grant_type",
    ],
    typing.Any,
]
