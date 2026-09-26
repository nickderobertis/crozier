

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextBodyAlign(enum.StrEnum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"

    def visit(
        self,
        left: typing.Callable[[], T_Result],
        center: typing.Callable[[], T_Result],
        right: typing.Callable[[], T_Result],
        justify: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextBodyAlign.LEFT:
            return left()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextBodyAlign.CENTER:
            return center()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextBodyAlign.RIGHT:
            return right()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextBodyAlign.JUSTIFY:
            return justify()
