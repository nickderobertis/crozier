

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemInkIntent(enum.StrEnum):
    INK_HIGHLIGHT = "ink-highlight"

    def visit(self, ink_highlight: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsList200ResponseAnnotationsItemInkIntent.INK_HIGHLIGHT:
            return ink_highlight()
