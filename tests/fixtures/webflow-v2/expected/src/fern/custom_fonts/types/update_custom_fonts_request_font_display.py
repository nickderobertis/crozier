

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateCustomFontsRequestFontDisplay(enum.StrEnum):
    """
    CSS font-display value
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
        if self is UpdateCustomFontsRequestFontDisplay.AUTO:
            return auto()
        if self is UpdateCustomFontsRequestFontDisplay.BLOCK:
            return block()
        if self is UpdateCustomFontsRequestFontDisplay.SWAP:
            return swap()
        if self is UpdateCustomFontsRequestFontDisplay.FALLBACK:
            return fallback()
        if self is UpdateCustomFontsRequestFontDisplay.OPTIONAL:
            return optional()
