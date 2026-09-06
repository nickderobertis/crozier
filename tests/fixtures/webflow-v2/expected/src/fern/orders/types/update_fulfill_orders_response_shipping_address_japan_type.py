

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateFulfillOrdersResponseShippingAddressJapanType(enum.StrEnum):
    """
    Represents a Japan-only address format. This field will only appear on orders placed from Japan.
    """

    KANA = "kana"
    KANJI = "kanji"

    def visit(self, kana: typing.Callable[[], T_Result], kanji: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateFulfillOrdersResponseShippingAddressJapanType.KANA:
            return kana()
        if self is UpdateFulfillOrdersResponseShippingAddressJapanType.KANJI:
            return kanji()
