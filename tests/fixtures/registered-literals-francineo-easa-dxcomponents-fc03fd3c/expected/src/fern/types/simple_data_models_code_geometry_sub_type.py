

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SimpleDataModelsCodeGeometrySubType(enum.StrEnum):
    """
    A string indicating what type of geometry sub-type is being provided. Currently supports only circle.
    """

    CIRCLE = "Circle"

    def visit(self, circle: typing.Callable[[], T_Result]) -> T_Result:
        if self is SimpleDataModelsCodeGeometrySubType.CIRCLE:
            return circle()
