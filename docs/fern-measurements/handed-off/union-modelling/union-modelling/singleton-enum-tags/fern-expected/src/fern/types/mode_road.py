

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModeRoad(enum.StrEnum):
    ROAD = "road"

    def visit(self, road: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModeRoad.ROAD:
            return road()
