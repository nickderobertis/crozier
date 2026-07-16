

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WritableRackWeightUnit(str, enum.Enum):
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
        if self is WritableRackWeightUnit.KG:
            return kg()
        if self is WritableRackWeightUnit.G:
            return g()
        if self is WritableRackWeightUnit.LB:
            return lb()
        if self is WritableRackWeightUnit.OZ:
            return oz()
