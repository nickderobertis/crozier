

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateCustomFontsRequestFontDisplay(enum.StrEnum):
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
        if self is CreateCustomFontsRequestFontDisplay.AUTO:
            return auto()
        if self is CreateCustomFontsRequestFontDisplay.BLOCK:
            return block()
        if self is CreateCustomFontsRequestFontDisplay.SWAP:
            return swap()
        if self is CreateCustomFontsRequestFontDisplay.FALLBACK:
            return fallback()
        if self is CreateCustomFontsRequestFontDisplay.OPTIONAL:
            return optional()
