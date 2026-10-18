

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProtocolErrorType(enum.StrEnum):
    ERROR = "error"

    def visit(self, error: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProtocolErrorType.ERROR:
            return error()
