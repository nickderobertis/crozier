

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DeviceTypeWeightUnitValue(str, enum.Enum):
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
        if self is DeviceTypeWeightUnitValue.KG:
            return kg()
        if self is DeviceTypeWeightUnitValue.G:
            return g()
        if self is DeviceTypeWeightUnitValue.LB:
            return lb()
        if self is DeviceTypeWeightUnitValue.OZ:
            return oz()
