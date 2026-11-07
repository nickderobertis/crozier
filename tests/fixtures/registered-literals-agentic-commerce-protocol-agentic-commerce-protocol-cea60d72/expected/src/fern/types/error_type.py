

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ErrorType(enum.StrEnum):
    INVALID_REQUEST = "invalid_request"
    REQUEST_NOT_IDEMPOTENT = "request_not_idempotent"
    PROCESSING_ERROR = "processing_error"
    SERVICE_UNAVAILABLE = "service_unavailable"

    def visit(
        self,
        invalid_request: typing.Callable[[], T_Result],
        request_not_idempotent: typing.Callable[[], T_Result],
        processing_error: typing.Callable[[], T_Result],
        service_unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ErrorType.INVALID_REQUEST:
            return invalid_request()
        if self is ErrorType.REQUEST_NOT_IDEMPOTENT:
            return request_not_idempotent()
        if self is ErrorType.PROCESSING_ERROR:
            return processing_error()
        if self is ErrorType.SERVICE_UNAVAILABLE:
            return service_unavailable()
