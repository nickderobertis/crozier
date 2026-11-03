

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListParcelsRequestCarrier(enum.StrEnum):
    ROAD = "road"
    RAIL = "rail"
    AIR = "air"

    def visit(
        self,
        road: typing.Callable[[], T_Result],
        rail: typing.Callable[[], T_Result],
        air: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListParcelsRequestCarrier.ROAD:
            return road()
        if self is ListParcelsRequestCarrier.RAIL:
            return rail()
        if self is ListParcelsRequestCarrier.AIR:
            return air()
