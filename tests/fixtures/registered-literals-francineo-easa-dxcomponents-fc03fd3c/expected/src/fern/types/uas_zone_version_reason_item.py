

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UasZoneVersionReasonItem(enum.StrEnum):
    AIR_TRAFFIC = "AIR_TRAFFIC"
    SENSITIVE = "SENSITIVE"
    PRIVACY = "PRIVACY"
    POPULATION = "POPULATION"
    NATURE = "NATURE"
    NOISE = "NOISE"
    EMERGENCY = "EMERGENCY"
    DAR = "DAR"
    OTHER = "OTHER"

    def visit(
        self,
        air_traffic: typing.Callable[[], T_Result],
        sensitive: typing.Callable[[], T_Result],
        privacy: typing.Callable[[], T_Result],
        population: typing.Callable[[], T_Result],
        nature: typing.Callable[[], T_Result],
        noise: typing.Callable[[], T_Result],
        emergency: typing.Callable[[], T_Result],
        dar: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UasZoneVersionReasonItem.AIR_TRAFFIC:
            return air_traffic()
        if self is UasZoneVersionReasonItem.SENSITIVE:
            return sensitive()
        if self is UasZoneVersionReasonItem.PRIVACY:
            return privacy()
        if self is UasZoneVersionReasonItem.POPULATION:
            return population()
        if self is UasZoneVersionReasonItem.NATURE:
            return nature()
        if self is UasZoneVersionReasonItem.NOISE:
            return noise()
        if self is UasZoneVersionReasonItem.EMERGENCY:
            return emergency()
        if self is UasZoneVersionReasonItem.DAR:
            return dar()
        if self is UasZoneVersionReasonItem.OTHER:
            return other()
