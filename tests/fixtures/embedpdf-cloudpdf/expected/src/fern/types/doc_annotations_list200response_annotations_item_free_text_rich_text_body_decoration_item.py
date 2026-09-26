

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBodyDecorationItem(enum.StrEnum):
    UNDERLINE = "underline"
    LINE_THROUGH = "line-through"
    WORD = "word"

    def visit(
        self,
        underline: typing.Callable[[], T_Result],
        line_through: typing.Callable[[], T_Result],
        word: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBodyDecorationItem.UNDERLINE:
            return underline()
        if self is DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBodyDecorationItem.LINE_THROUGH:
            return line_through()
        if self is DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBodyDecorationItem.WORD:
            return word()
