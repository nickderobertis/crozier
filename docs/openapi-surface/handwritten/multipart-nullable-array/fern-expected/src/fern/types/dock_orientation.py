

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DockOrientation(enum.StrEnum):
    NORTH = "north"
    SOUTH = "south"

    def visit(self, north: typing.Callable[[], T_Result], south: typing.Callable[[], T_Result]) -> T_Result:
        if self is DockOrientation.NORTH:
            return north()
        if self is DockOrientation.SOUTH:
            return south()
