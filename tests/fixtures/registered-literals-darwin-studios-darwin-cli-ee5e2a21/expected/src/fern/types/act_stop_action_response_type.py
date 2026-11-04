

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActStopActionResponseType(enum.StrEnum):
    STOP = "stop"

    def visit(self, stop: typing.Callable[[], T_Result]) -> T_Result:
        if self is ActStopActionResponseType.STOP:
            return stop()
