

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemPolylineIntent(enum.StrEnum):
    POLY_LINE_DIMENSION = "PolyLineDimension"

    def visit(self, poly_line_dimension: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsList200ResponseAnnotationsItemPolylineIntent.POLY_LINE_DIMENSION:
            return poly_line_dimension()
