

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DistanceUnit(enum.StrEnum):
    """
    DistanceUnit defines the unit for distance calculation: kilometers or miles.
    """

    KILOMETERS = "Kilometers"
    MILES = "Miles"

    def visit(self, kilometers: typing.Callable[[], T_Result], miles: typing.Callable[[], T_Result]) -> T_Result:
        if self is DistanceUnit.KILOMETERS:
            return kilometers()
        if self is DistanceUnit.MILES:
            return miles()
