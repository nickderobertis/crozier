

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EnergyType(enum.StrEnum):
    """
    Energy type present on the vehicle.
    """

    FUEL = "Fuel"
    ELECTRIC = "Electric"

    def visit(self, fuel: typing.Callable[[], T_Result], electric: typing.Callable[[], T_Result]) -> T_Result:
        if self is EnergyType.FUEL:
            return fuel()
        if self is EnergyType.ELECTRIC:
            return electric()
