

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemWidgetBorderStyle(enum.StrEnum):
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
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetBorderStyle.SOLID:
            return solid()
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetBorderStyle.DASHED:
            return dashed()
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetBorderStyle.BEVELED:
            return beveled()
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetBorderStyle.INSET:
            return inset()
