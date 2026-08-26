

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RoadOperatorRoadOperatorType(enum.StrEnum):
    """
    The road operator type.
    """

    WATER_AUTHORITY = "WaterAuthority"
    MUNICIPALITY = "Municipality"
    PROVINCE = "Province"
    STATE = "State"
    OTHER = "Other"

    def visit(
        self,
        water_authority: typing.Callable[[], T_Result],
        municipality: typing.Callable[[], T_Result],
        province: typing.Callable[[], T_Result],
        state: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RoadOperatorRoadOperatorType.WATER_AUTHORITY:
            return water_authority()
        if self is RoadOperatorRoadOperatorType.MUNICIPALITY:
            return municipality()
        if self is RoadOperatorRoadOperatorType.PROVINCE:
            return province()
        if self is RoadOperatorRoadOperatorType.STATE:
            return state()
        if self is RoadOperatorRoadOperatorType.OTHER:
            return other()
