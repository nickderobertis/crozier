

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ViewOptionsOptionsOptionsSpanType(enum.StrEnum):
    RANGE = "range"
    FRAME = "frame"

    def visit(self, range: typing.Callable[[], T_Result], frame: typing.Callable[[], T_Result]) -> T_Result:
        if self is ViewOptionsOptionsOptionsSpanType.RANGE:
            return range()
        if self is ViewOptionsOptionsOptionsSpanType.FRAME:
            return frame()
