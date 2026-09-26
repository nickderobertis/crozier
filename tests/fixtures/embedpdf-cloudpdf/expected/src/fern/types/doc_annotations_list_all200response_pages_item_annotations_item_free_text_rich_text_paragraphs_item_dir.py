

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextParagraphsItemDir(enum.StrEnum):
    LTR = "ltr"
    RTL = "rtl"

    def visit(self, ltr: typing.Callable[[], T_Result], rtl: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextParagraphsItemDir.LTR:
            return ltr()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextParagraphsItemDir.RTL:
            return rtl()
