

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ModuleTypeWeightUnitLabel(str, enum.Enum):
    KILOGRAMS = "Kilograms"
    GRAMS = "Grams"
    POUNDS = "Pounds"
    OUNCES = "Ounces"

    def visit(
        self,
        kilograms: typing.Callable[[], T_Result],
        grams: typing.Callable[[], T_Result],
        pounds: typing.Callable[[], T_Result],
        ounces: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ModuleTypeWeightUnitLabel.KILOGRAMS:
            return kilograms()
        if self is ModuleTypeWeightUnitLabel.GRAMS:
            return grams()
        if self is ModuleTypeWeightUnitLabel.POUNDS:
            return pounds()
        if self is ModuleTypeWeightUnitLabel.OUNCES:
            return ounces()
