

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GlazeKind(enum.StrEnum):
    CLEAR = "clear"
    COBALT = "cobalt"

    def visit(self, clear: typing.Callable[[], T_Result], cobalt: typing.Callable[[], T_Result]) -> T_Result:
        if self is GlazeKind.CLEAR:
            return clear()
        if self is GlazeKind.COBALT:
            return cobalt()
