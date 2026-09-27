

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MotionRequestOneActionThree(enum.StrEnum):
    CLEAR = "clear"

    def visit(self, clear: typing.Callable[[], T_Result]) -> T_Result:
        if self is MotionRequestOneActionThree.CLEAR:
            return clear()
