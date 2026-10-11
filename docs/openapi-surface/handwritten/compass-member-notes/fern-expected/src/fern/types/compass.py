

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Compass(enum.StrEnum):
    NORTH = "north"
    SOUTH = "south"
    """
    Towards the southern horizon.
    """

    def visit(self, north: typing.Callable[[], T_Result], south: typing.Callable[[], T_Result]) -> T_Result:
        if self is Compass.NORTH:
            return north()
        if self is Compass.SOUTH:
            return south()
