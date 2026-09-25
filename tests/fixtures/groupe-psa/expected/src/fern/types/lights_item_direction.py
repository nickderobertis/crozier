

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LightsItemDirection(enum.StrEnum):
    LEFT = "Left"
    RIGHT = "Right"

    def visit(self, left: typing.Callable[[], T_Result], right: typing.Callable[[], T_Result]) -> T_Result:
        if self is LightsItemDirection.LEFT:
            return left()
        if self is LightsItemDirection.RIGHT:
            return right()
