

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class BatchCreateCustomFontsResponseCreatedItemCustomFontFontDisplay(enum.StrEnum):
    """
    The CSS font-display value
    """

    AUTO = "auto"
    BLOCK = "block"
    SWAP = "swap"
    FALLBACK = "fallback"
    OPTIONAL = "optional"

    def visit(
        self,
        auto: typing.Callable[[], T_Result],
        block: typing.Callable[[], T_Result],
        swap: typing.Callable[[], T_Result],
        fallback: typing.Callable[[], T_Result],
        optional: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BatchCreateCustomFontsResponseCreatedItemCustomFontFontDisplay.AUTO:
            return auto()
        if self is BatchCreateCustomFontsResponseCreatedItemCustomFontFontDisplay.BLOCK:
            return block()
        if self is BatchCreateCustomFontsResponseCreatedItemCustomFontFontDisplay.SWAP:
            return swap()
        if self is BatchCreateCustomFontsResponseCreatedItemCustomFontFontDisplay.FALLBACK:
            return fallback()
        if self is BatchCreateCustomFontsResponseCreatedItemCustomFontFontDisplay.OPTIONAL:
            return optional()
