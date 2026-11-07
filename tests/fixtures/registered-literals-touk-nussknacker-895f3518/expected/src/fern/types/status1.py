

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Status1(enum.StrEnum):
    ERROR = "ERROR"

    def visit(self, error: typing.Callable[[], T_Result]) -> T_Result:
        if self is Status1.ERROR:
            return error()
