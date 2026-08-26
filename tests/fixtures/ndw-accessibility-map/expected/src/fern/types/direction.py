

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Direction(enum.StrEnum):
    """
    Direction of travel
    """

    FORWARD = "forward"
    BACKWARD = "backward"

    def visit(self, forward: typing.Callable[[], T_Result], backward: typing.Callable[[], T_Result]) -> T_Result:
        if self is Direction.FORWARD:
            return forward()
        if self is Direction.BACKWARD:
            return backward()
