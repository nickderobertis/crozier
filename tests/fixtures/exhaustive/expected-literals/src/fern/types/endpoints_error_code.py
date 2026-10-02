

import typing

EndpointsErrorCode = typing.Union[
    typing.Literal[
        "INTERNAL_SERVER_ERROR",
        "UNAUTHORIZED",
        "FORBIDDEN",
        "BAD_REQUEST",
        "CONFLICT",
        "GONE",
        "UNPROCESSABLE_ENTITY",
        "NOT_IMPLEMENTED",
        "BAD_GATEWAY",
        "SERVICE_UNAVAILABLE",
        "Unknown",
    ],
    typing.Any,
]
