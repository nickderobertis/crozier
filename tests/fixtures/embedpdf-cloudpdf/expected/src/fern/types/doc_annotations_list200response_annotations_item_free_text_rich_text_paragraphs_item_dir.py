

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextParagraphsItemDir(enum.StrEnum):
    LTR = "ltr"
    RTL = "rtl"

    def visit(self, ltr: typing.Callable[[], T_Result], rtl: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextParagraphsItemDir.LTR:
            return ltr()
        if self is DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextParagraphsItemDir.RTL:
            return rtl()
