

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RelativeTimeRangeConfigModelRelativeTimeType(enum.StrEnum):
    """
    Direction in which to count time. Default = BACKWARD
    """

    BACKWARD = "BACKWARD"
    FORWARD = "FORWARD"

    def visit(self, backward: typing.Callable[[], T_Result], forward: typing.Callable[[], T_Result]) -> T_Result:
        if self is RelativeTimeRangeConfigModelRelativeTimeType.BACKWARD:
            return backward()
        if self is RelativeTimeRangeConfigModelRelativeTimeType.FORWARD:
            return forward()
