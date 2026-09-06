

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ReplaceFileCustomFontsResponseCustomFontFontDisplay(enum.StrEnum):
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
        if self is ReplaceFileCustomFontsResponseCustomFontFontDisplay.AUTO:
            return auto()
        if self is ReplaceFileCustomFontsResponseCustomFontFontDisplay.BLOCK:
            return block()
        if self is ReplaceFileCustomFontsResponseCustomFontFontDisplay.SWAP:
            return swap()
        if self is ReplaceFileCustomFontsResponseCustomFontFontDisplay.FALLBACK:
            return fallback()
        if self is ReplaceFileCustomFontsResponseCustomFontFontDisplay.OPTIONAL:
            return optional()
