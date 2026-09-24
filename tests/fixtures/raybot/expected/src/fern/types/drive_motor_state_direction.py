

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DriveMotorStateDirection(enum.StrEnum):
    """
    The direction of the drive motor
    """

    FORWARD = "FORWARD"
    BACKWARD = "BACKWARD"

    def visit(self, forward: typing.Callable[[], T_Result], backward: typing.Callable[[], T_Result]) -> T_Result:
        if self is DriveMotorStateDirection.FORWARD:
            return forward()
        if self is DriveMotorStateDirection.BACKWARD:
            return backward()
