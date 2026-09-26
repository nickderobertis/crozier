

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextIntent(enum.StrEnum):
    FREE_TEXT = "free-text"
    FREE_TEXT_CALLOUT = "free-text-callout"

    def visit(
        self, free_text: typing.Callable[[], T_Result], free_text_callout: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextIntent.FREE_TEXT:
            return free_text()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextIntent.FREE_TEXT_CALLOUT:
            return free_text_callout()
