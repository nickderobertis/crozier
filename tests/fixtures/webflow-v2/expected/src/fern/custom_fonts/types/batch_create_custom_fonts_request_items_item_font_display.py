

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class BatchCreateCustomFontsRequestItemsItemFontDisplay(enum.StrEnum):
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
        if self is BatchCreateCustomFontsRequestItemsItemFontDisplay.AUTO:
            return auto()
        if self is BatchCreateCustomFontsRequestItemsItemFontDisplay.BLOCK:
            return block()
        if self is BatchCreateCustomFontsRequestItemsItemFontDisplay.SWAP:
            return swap()
        if self is BatchCreateCustomFontsRequestItemsItemFontDisplay.FALLBACK:
            return fallback()
        if self is BatchCreateCustomFontsRequestItemsItemFontDisplay.OPTIONAL:
            return optional()
