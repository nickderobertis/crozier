

import typing

ErrorResponseDtoError = typing.Union[
    typing.Literal[
        "invalid_request",
        "invalid_client",
        "invalid_grant",
        "unauthorized_client",
        "unsupported_grant_type",
        "invalid_scope",
        "access_denied",
    ],
    typing.Any,
]
