

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VehicleItemMotorization(enum.StrEnum):
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
        if self is VehicleItemMotorization.ELECTRIC:
            return electric()
        if self is VehicleItemMotorization.HYBRID:
            return hybrid()
        if self is VehicleItemMotorization.THERMIC:
            return thermic()
        if self is VehicleItemMotorization.HYDROGEN:
            return hydrogen()
