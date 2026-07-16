

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class RackOuterUnitLabel(str, enum.Enum):
    MILLIMETERS = "Millimeters"
    INCHES = "Inches"

    def visit(self, millimeters: typing.Callable[[], T_Result], inches: typing.Callable[[], T_Result]) -> T_Result:
        if self is RackOuterUnitLabel.MILLIMETERS:
            return millimeters()
        if self is RackOuterUnitLabel.INCHES:
            return inches()
