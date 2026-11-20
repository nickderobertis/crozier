

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VentAlertMotor(enum.StrEnum):
    """
    The motor that drove the vent.
    """

    NORTH = "north"
    SOUTH = "south"

    def visit(self, north: typing.Callable[[], T_Result], south: typing.Callable[[], T_Result]) -> T_Result:
        if self is VentAlertMotor.NORTH:
            return north()
        if self is VentAlertMotor.SOUTH:
            return south()
