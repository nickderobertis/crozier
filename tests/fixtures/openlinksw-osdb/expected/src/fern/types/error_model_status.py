

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ErrorModelStatus(enum.StrEnum):
    ERROR = "error"

    def visit(self, error: typing.Callable[[], T_Result]) -> T_Result:
        if self is ErrorModelStatus.ERROR:
            return error()
