

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EventVesselDepartedType(enum.StrEnum):
    VESSEL_DEPARTED = "vessel.departed"

    def visit(self, vessel_departed: typing.Callable[[], T_Result]) -> T_Result:
        if self is EventVesselDepartedType.VESSEL_DEPARTED:
            return vessel_departed()
