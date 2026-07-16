

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WritableDeviceTypeWeightUnit(enum.StrEnum):
    KG = "kg"
    G = "g"
    LB = "lb"
    OZ = "oz"

    def visit(
        self,
        kg: typing.Callable[[], T_Result],
        g: typing.Callable[[], T_Result],
        lb: typing.Callable[[], T_Result],
        oz: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WritableDeviceTypeWeightUnit.KG:
            return kg()
        if self is WritableDeviceTypeWeightUnit.G:
            return g()
        if self is WritableDeviceTypeWeightUnit.LB:
            return lb()
        if self is WritableDeviceTypeWeightUnit.OZ:
            return oz()
