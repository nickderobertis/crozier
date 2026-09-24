

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CargoDoorMotorStateDirection(enum.StrEnum):
    """
    The direction of the cargo door motor
    """

    CLOSE = "CLOSE"
    OPEN = "OPEN"

    def visit(self, close: typing.Callable[[], T_Result], open: typing.Callable[[], T_Result]) -> T_Result:
        if self is CargoDoorMotorStateDirection.CLOSE:
            return close()
        if self is CargoDoorMotorStateDirection.OPEN:
            return open()
