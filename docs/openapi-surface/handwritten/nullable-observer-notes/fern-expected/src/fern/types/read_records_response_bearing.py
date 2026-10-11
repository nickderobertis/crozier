

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReadRecordsResponseBearing(enum.StrEnum):
    """
    The observed bearing.
    """

    EAST = "east"
    WEST = "west"

    def visit(self, east: typing.Callable[[], T_Result], west: typing.Callable[[], T_Result]) -> T_Result:
        if self is ReadRecordsResponseBearing.EAST:
            return east()
        if self is ReadRecordsResponseBearing.WEST:
            return west()
