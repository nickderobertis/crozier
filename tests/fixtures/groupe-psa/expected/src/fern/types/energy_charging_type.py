

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EnergyChargingType(enum.StrEnum):
    """
    Charging type associated to the vehicle. Full means that the charge will stop when it is completed whereas partial will stop before end of charge in order to optimize battery lifetime.
    """

    PARTIAL = "Partial"
    FULL = "Full"

    def visit(self, partial: typing.Callable[[], T_Result], full: typing.Callable[[], T_Result]) -> T_Result:
        if self is EnergyChargingType.PARTIAL:
            return partial()
        if self is EnergyChargingType.FULL:
            return full()
