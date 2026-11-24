

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListZonesRequestKind(enum.StrEnum):
    LAND = "land"
    SEA = "sea"

    def visit(self, land: typing.Callable[[], T_Result], sea: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListZonesRequestKind.LAND:
            return land()
        if self is ListZonesRequestKind.SEA:
            return sea()
