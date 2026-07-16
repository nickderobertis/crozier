

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeviceTypeWeightUnitLabel(enum.StrEnum):
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
        if self is DeviceTypeWeightUnitLabel.KILOGRAMS:
            return kilograms()
        if self is DeviceTypeWeightUnitLabel.GRAMS:
            return grams()
        if self is DeviceTypeWeightUnitLabel.POUNDS:
            return pounds()
        if self is DeviceTypeWeightUnitLabel.OUNCES:
            return ounces()
