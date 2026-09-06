

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetCustomFontsResponseCustomFontFontDisplay(enum.StrEnum):
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
        if self is GetCustomFontsResponseCustomFontFontDisplay.AUTO:
            return auto()
        if self is GetCustomFontsResponseCustomFontFontDisplay.BLOCK:
            return block()
        if self is GetCustomFontsResponseCustomFontFontDisplay.SWAP:
            return swap()
        if self is GetCustomFontsResponseCustomFontFontDisplay.FALLBACK:
            return fallback()
        if self is GetCustomFontsResponseCustomFontFontDisplay.OPTIONAL:
            return optional()
