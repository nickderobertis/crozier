

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PassageLane(enum.StrEnum):
    """
    The first member already satisfies the pattern.
    """

    EAST = "east"
    WEST = "west"

    def visit(self, east: typing.Callable[[], T_Result], west: typing.Callable[[], T_Result]) -> T_Result:
        if self is PassageLane.EAST:
            return east()
        if self is PassageLane.WEST:
            return west()
