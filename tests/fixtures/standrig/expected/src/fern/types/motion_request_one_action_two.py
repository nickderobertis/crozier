

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MotionRequestOneActionTwo(enum.StrEnum):
    STOP = "stop"

    def visit(self, stop: typing.Callable[[], T_Result]) -> T_Result:
        if self is MotionRequestOneActionTwo.STOP:
            return stop()
