

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SimpleDataModelsCodeZoneReasonTypeItem(enum.StrEnum):
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
        if self is SimpleDataModelsCodeZoneReasonTypeItem.AIR_TRAFFIC:
            return air_traffic()
        if self is SimpleDataModelsCodeZoneReasonTypeItem.SENSITIVE:
            return sensitive()
        if self is SimpleDataModelsCodeZoneReasonTypeItem.PRIVACY:
            return privacy()
        if self is SimpleDataModelsCodeZoneReasonTypeItem.POPULATION:
            return population()
        if self is SimpleDataModelsCodeZoneReasonTypeItem.NATURE:
            return nature()
        if self is SimpleDataModelsCodeZoneReasonTypeItem.NOISE:
            return noise()
        if self is SimpleDataModelsCodeZoneReasonTypeItem.EMERGENCY:
            return emergency()
        if self is SimpleDataModelsCodeZoneReasonTypeItem.DAR:
            return dar()
        if self is SimpleDataModelsCodeZoneReasonTypeItem.OTHER:
            return other()
