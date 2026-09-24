

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MoveDirection(enum.StrEnum):
    """
    The direction when moving
    """

    FORWARD = "FORWARD"
    BACKWARD = "BACKWARD"

    def visit(self, forward: typing.Callable[[], T_Result], backward: typing.Callable[[], T_Result]) -> T_Result:
        if self is MoveDirection.FORWARD:
            return forward()
        if self is MoveDirection.BACKWARD:
            return backward()
