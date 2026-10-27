

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelsOne(enum.StrEnum):
    SOUTH = "south"

    def visit(self, south: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChannelsOne.SOUTH:
            return south()
