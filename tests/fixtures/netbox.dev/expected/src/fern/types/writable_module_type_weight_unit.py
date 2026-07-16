

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WritableModuleTypeWeightUnit(str, enum.Enum):
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
        if self is WritableModuleTypeWeightUnit.KG:
            return kg()
        if self is WritableModuleTypeWeightUnit.G:
            return g()
        if self is WritableModuleTypeWeightUnit.LB:
            return lb()
        if self is WritableModuleTypeWeightUnit.OZ:
            return oz()
