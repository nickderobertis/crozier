

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemLineIntent(enum.StrEnum):
    LINE_ARROW = "LineArrow"
    LINE_DIMENSION = "LineDimension"

    def visit(
        self, line_arrow: typing.Callable[[], T_Result], line_dimension: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is DocAnnotationsList200ResponseAnnotationsItemLineIntent.LINE_ARROW:
            return line_arrow()
        if self is DocAnnotationsList200ResponseAnnotationsItemLineIntent.LINE_DIMENSION:
            return line_dimension()
