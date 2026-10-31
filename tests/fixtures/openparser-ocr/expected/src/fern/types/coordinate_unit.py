

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CoordinateUnit(enum.StrEnum):
    PIXEL = "pixel"
    POINT = "point"
    INCH = "inch"
    NORMALIZED = "normalized"

    def visit(
        self,
        pixel: typing.Callable[[], T_Result],
        point: typing.Callable[[], T_Result],
        inch: typing.Callable[[], T_Result],
        normalized: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CoordinateUnit.PIXEL:
            return pixel()
        if self is CoordinateUnit.POINT:
            return point()
        if self is CoordinateUnit.INCH:
            return inch()
        if self is CoordinateUnit.NORMALIZED:
            return normalized()
