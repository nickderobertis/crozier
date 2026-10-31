

import typing

DefaultErrorDataCode = typing.Union[
    typing.Literal[
        "PARSE_ERROR",
        "BAD_REQUEST",
        "INTERNAL_SERVER_ERROR",
        "NOT_IMPLEMENTED",
        "BAD_GATEWAY",
        "SERVICE_UNAVAILABLE",
        "GATEWAY_TIMEOUT",
        "UNAUTHORIZED",
        "PAYMENT_REQUIRED",
        "FORBIDDEN",
        "NOT_FOUND",
        "METHOD_NOT_SUPPORTED",
        "TIMEOUT",
        "CONFLICT",
        "PRECONDITION_FAILED",
        "PAYLOAD_TOO_LARGE",
        "UNSUPPORTED_MEDIA_TYPE",
        "UNPROCESSABLE_CONTENT",
        "PRECONDITION_REQUIRED",
        "TOO_MANY_REQUESTS",
        "CLIENT_CLOSED_REQUEST",
    ],
    typing.Any,
]
