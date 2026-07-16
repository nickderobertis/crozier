

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CableLengthUnitLabel(enum.StrEnum):
    KILOMETERS = "Kilometers"
    METERS = "Meters"
    CENTIMETERS = "Centimeters"
    MILES = "Miles"
    FEET = "Feet"
    INCHES = "Inches"

    def visit(
        self,
        kilometers: typing.Callable[[], T_Result],
        meters: typing.Callable[[], T_Result],
        centimeters: typing.Callable[[], T_Result],
        miles: typing.Callable[[], T_Result],
        feet: typing.Callable[[], T_Result],
        inches: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CableLengthUnitLabel.KILOMETERS:
            return kilometers()
        if self is CableLengthUnitLabel.METERS:
            return meters()
        if self is CableLengthUnitLabel.CENTIMETERS:
            return centimeters()
        if self is CableLengthUnitLabel.MILES:
            return miles()
        if self is CableLengthUnitLabel.FEET:
            return feet()
        if self is CableLengthUnitLabel.INCHES:
            return inches()
