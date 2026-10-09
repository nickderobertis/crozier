

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostRouteChangedPayloadReason(enum.StrEnum):
    WEATHER = "weather"
    TRAFFIC = "traffic"
    DEPOT = "depot"

    def visit(
        self,
        weather: typing.Callable[[], T_Result],
        traffic: typing.Callable[[], T_Result],
        depot: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostRouteChangedPayloadReason.WEATHER:
            return weather()
        if self is PostRouteChangedPayloadReason.TRAFFIC:
            return traffic()
        if self is PostRouteChangedPayloadReason.DEPOT:
            return depot()
