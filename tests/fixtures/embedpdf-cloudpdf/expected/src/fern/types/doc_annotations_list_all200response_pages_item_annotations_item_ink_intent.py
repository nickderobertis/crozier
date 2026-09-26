

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkIntent(enum.StrEnum):
    INK_HIGHLIGHT = "ink-highlight"

    def visit(self, ink_highlight: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkIntent.INK_HIGHLIGHT:
            return ink_highlight()
