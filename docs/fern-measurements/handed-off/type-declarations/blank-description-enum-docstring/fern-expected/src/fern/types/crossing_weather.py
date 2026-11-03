

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CrossingWeather(enum.StrEnum):
    """ """

    CALM = "CALM"
    ROUGH = "ROUGH"

    def visit(self, calm: typing.Callable[[], T_Result], rough: typing.Callable[[], T_Result]) -> T_Result:
        if self is CrossingWeather.CALM:
            return calm()
        if self is CrossingWeather.ROUGH:
            return rough()
