

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextParagraphsItemRunsItemStyleScript(
    enum.StrEnum
):
    NORMAL = "normal"
    SUB = "sub"
    SUPER = "super"

    def visit(
        self,
        normal: typing.Callable[[], T_Result],
        sub: typing.Callable[[], T_Result],
        super: typing.Callable[[], T_Result],
    ) -> T_Result:
        if (
            self
            is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextParagraphsItemRunsItemStyleScript.NORMAL
        ):
            return normal()
        if (
            self
            is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextParagraphsItemRunsItemStyleScript.SUB
        ):
            return sub()
        if (
            self
            is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextParagraphsItemRunsItemStyleScript.SUPER
        ):
            return super()
