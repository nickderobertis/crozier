

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListLettersRequestCarrier(enum.StrEnum):
    ROAD = "road"
    RAIL = "rail"
    AIR = "air"

    def visit(
        self,
        road: typing.Callable[[], T_Result],
        rail: typing.Callable[[], T_Result],
        air: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListLettersRequestCarrier.ROAD:
            return road()
        if self is ListLettersRequestCarrier.RAIL:
            return rail()
        if self is ListLettersRequestCarrier.AIR:
            return air()
