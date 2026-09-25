

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EnergyBaseType(enum.StrEnum):
    """
    Energy type present on the vehicle.
    """

    FUEL = "Fuel"
    ELECTRIC = "Electric"

    def visit(self, fuel: typing.Callable[[], T_Result], electric: typing.Callable[[], T_Result]) -> T_Result:
        if self is EnergyBaseType.FUEL:
            return fuel()
        if self is EnergyBaseType.ELECTRIC:
            return electric()
