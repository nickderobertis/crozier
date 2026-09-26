

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBodyAlign(enum.StrEnum):
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
        if self is DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBodyAlign.LEFT:
            return left()
        if self is DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBodyAlign.CENTER:
            return center()
        if self is DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBodyAlign.RIGHT:
            return right()
        if self is DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBodyAlign.JUSTIFY:
            return justify()
