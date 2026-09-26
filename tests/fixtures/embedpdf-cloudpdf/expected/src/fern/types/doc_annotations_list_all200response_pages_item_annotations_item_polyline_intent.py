

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineIntent(enum.StrEnum):
    POLY_LINE_DIMENSION = "PolyLineDimension"

    def visit(self, poly_line_dimension: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineIntent.POLY_LINE_DIMENSION:
            return poly_line_dimension()
