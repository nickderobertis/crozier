

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BadRequestErrorBodyErrorType(enum.StrEnum):
    INVALID_REQUEST_ERROR = "invalid_request_error"

    def visit(self, invalid_request_error: typing.Callable[[], T_Result]) -> T_Result:
        if self is BadRequestErrorBodyErrorType.INVALID_REQUEST_ERROR:
            return invalid_request_error()
