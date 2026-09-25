

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ErrorResponseStatus(enum.StrEnum):
    ERROR = "error"

    def visit(self, error: typing.Callable[[], T_Result]) -> T_Result:
        if self is ErrorResponseStatus.ERROR:
            return error()
