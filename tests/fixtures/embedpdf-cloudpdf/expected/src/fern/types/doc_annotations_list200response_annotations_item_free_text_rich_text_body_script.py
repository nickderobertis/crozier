

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBodyScript(enum.StrEnum):
    NORMAL = "normal"
    SUB = "sub"
    SUPER = "super"

    def visit(
        self,
        normal: typing.Callable[[], T_Result],
        sub: typing.Callable[[], T_Result],
        super: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBodyScript.NORMAL:
            return normal()
        if self is DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBodyScript.SUB:
            return sub()
        if self is DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBodyScript.SUPER:
            return super()
