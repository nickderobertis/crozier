

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Lamp(enum.StrEnum):
    OIL_WICK = "oil wick"
    ELECTRIC = "electric"
    GAS_MANTLE = "gas mantle"

    def visit(
        self,
        oil_wick: typing.Callable[[], T_Result],
        electric: typing.Callable[[], T_Result],
        gas_mantle: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Lamp.OIL_WICK:
            return oil_wick()
        if self is Lamp.ELECTRIC:
            return electric()
        if self is Lamp.GAS_MANTLE:
            return gas_mantle()
