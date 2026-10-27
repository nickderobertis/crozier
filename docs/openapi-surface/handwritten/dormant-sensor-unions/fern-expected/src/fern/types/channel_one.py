

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelOne(enum.StrEnum):
    NORTH = "north"
    SOUTH = "south"

    def visit(self, north: typing.Callable[[], T_Result], south: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChannelOne.NORTH:
            return north()
        if self is ChannelOne.SOUTH:
            return south()
