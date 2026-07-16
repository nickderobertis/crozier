

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ModuleTypeWeightUnitValue(str, enum.Enum):
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
        if self is ModuleTypeWeightUnitValue.KG:
            return kg()
        if self is ModuleTypeWeightUnitValue.G:
            return g()
        if self is ModuleTypeWeightUnitValue.LB:
            return lb()
        if self is ModuleTypeWeightUnitValue.OZ:
            return oz()
