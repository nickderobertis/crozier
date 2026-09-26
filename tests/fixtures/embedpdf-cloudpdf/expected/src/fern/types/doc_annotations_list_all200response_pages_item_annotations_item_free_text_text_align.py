

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextTextAlign(enum.StrEnum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"

    def visit(
        self,
        left: typing.Callable[[], T_Result],
        center: typing.Callable[[], T_Result],
        right: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextTextAlign.LEFT:
            return left()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextTextAlign.CENTER:
            return center()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextTextAlign.RIGHT:
            return right()
