

import typing

ErrorType = typing.Union[
    typing.Literal["invalid_request", "request_not_idempotent", "processing_error", "service_unavailable"], typing.Any
]
