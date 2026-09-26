

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineIntent(enum.StrEnum):
    LINE_ARROW = "LineArrow"
    LINE_DIMENSION = "LineDimension"

    def visit(
        self, line_arrow: typing.Callable[[], T_Result], line_dimension: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineIntent.LINE_ARROW:
            return line_arrow()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineIntent.LINE_DIMENSION:
            return line_dimension()
