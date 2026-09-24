

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VehicleMotorization(enum.StrEnum):
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
        if self is VehicleMotorization.ELECTRIC:
            return electric()
        if self is VehicleMotorization.HYBRID:
            return hybrid()
        if self is VehicleMotorization.THERMIC:
            return thermic()
        if self is VehicleMotorization.HYDROGEN:
            return hydrogen()
