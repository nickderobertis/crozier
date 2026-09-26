

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemWidgetTextAlign(enum.StrEnum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"

    def visit(
        self,
        left: typing.Callable[[], T_Result],
        center: typing.Callable[[], T_Result],
        right: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetTextAlign.LEFT:
            return left()
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetTextAlign.CENTER:
            return center()
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetTextAlign.RIGHT:
            return right()
