

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EmissionZoneType(enum.StrEnum):
    ZERO_EMISSION_ZONE = "zero_emission_zone"
    LOW_EMISSION_ZONE = "low_emission_zone"

    def visit(
        self, zero_emission_zone: typing.Callable[[], T_Result], low_emission_zone: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is EmissionZoneType.ZERO_EMISSION_ZONE:
            return zero_emission_zone()
        if self is EmissionZoneType.LOW_EMISSION_ZONE:
            return low_emission_zone()
