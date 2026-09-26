

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetTextAlign(enum.StrEnum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"

    def visit(
        self,
        left: typing.Callable[[], T_Result],
        center: typing.Callable[[], T_Result],
        right: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetTextAlign.LEFT:
            return left()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetTextAlign.CENTER:
            return center()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetTextAlign.RIGHT:
            return right()
