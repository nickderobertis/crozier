

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemPolylineBorderStyle(enum.StrEnum):
    SOLID = "solid"
    DASHED = "dashed"
    BEVELED = "beveled"
    INSET = "inset"

    def visit(
        self,
        solid: typing.Callable[[], T_Result],
        dashed: typing.Callable[[], T_Result],
        beveled: typing.Callable[[], T_Result],
        inset: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocAnnotationsList200ResponseAnnotationsItemPolylineBorderStyle.SOLID:
            return solid()
        if self is DocAnnotationsList200ResponseAnnotationsItemPolylineBorderStyle.DASHED:
            return dashed()
        if self is DocAnnotationsList200ResponseAnnotationsItemPolylineBorderStyle.BEVELED:
            return beveled()
        if self is DocAnnotationsList200ResponseAnnotationsItemPolylineBorderStyle.INSET:
            return inset()
