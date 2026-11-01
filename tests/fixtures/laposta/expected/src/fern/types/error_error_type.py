

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ErrorErrorType(enum.StrEnum):
    INVALID_REQUEST = "invalid_request"
    INVALID_INPUT = "invalid_input"
    INTERNAL = "internal"

    def visit(
        self,
        invalid_request: typing.Callable[[], T_Result],
        invalid_input: typing.Callable[[], T_Result],
        internal: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ErrorErrorType.INVALID_REQUEST:
            return invalid_request()
        if self is ErrorErrorType.INVALID_INPUT:
            return invalid_input()
        if self is ErrorErrorType.INTERNAL:
            return internal()
