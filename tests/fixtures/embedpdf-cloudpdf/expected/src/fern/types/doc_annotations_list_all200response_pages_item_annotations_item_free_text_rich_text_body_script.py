

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextBodyScript(enum.StrEnum):
    NORMAL = "normal"
    SUB = "sub"
    SUPER = "super"

    def visit(
        self,
        normal: typing.Callable[[], T_Result],
        sub: typing.Callable[[], T_Result],
        super: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextBodyScript.NORMAL:
            return normal()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextBodyScript.SUB:
            return sub()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextBodyScript.SUPER:
            return super()
