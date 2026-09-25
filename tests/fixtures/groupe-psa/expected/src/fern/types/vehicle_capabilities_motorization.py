

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VehicleCapabilitiesMotorization(enum.StrEnum):
    """
    Motorization of the vehicle.
    """

    ELECTRIC = "Electric"
    HYBRID = "Hybrid"
    THERMIC = "Thermic"
    HYDROGEN = "Hydrogen"

    def visit(
        self,
        electric: typing.Callable[[], T_Result],
        hybrid: typing.Callable[[], T_Result],
        thermic: typing.Callable[[], T_Result],
        hydrogen: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VehicleCapabilitiesMotorization.ELECTRIC:
            return electric()
        if self is VehicleCapabilitiesMotorization.HYBRID:
            return hybrid()
        if self is VehicleCapabilitiesMotorization.THERMIC:
            return thermic()
        if self is VehicleCapabilitiesMotorization.HYDROGEN:
            return hydrogen()
