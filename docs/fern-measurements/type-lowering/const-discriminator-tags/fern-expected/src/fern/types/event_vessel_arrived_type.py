

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EventVesselArrivedType(enum.StrEnum):
    VESSEL_ARRIVED = "vessel.arrived"

    def visit(self, vessel_arrived: typing.Callable[[], T_Result]) -> T_Result:
        if self is EventVesselArrivedType.VESSEL_ARRIVED:
            return vessel_arrived()
