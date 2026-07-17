

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RackWeightUnitLabel(enum.StrEnum):
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
        if self is RackWeightUnitLabel.KILOGRAMS:
            return kilograms()
        if self is RackWeightUnitLabel.GRAMS:
            return grams()
        if self is RackWeightUnitLabel.POUNDS:
            return pounds()
        if self is RackWeightUnitLabel.OUNCES:
            return ounces()
