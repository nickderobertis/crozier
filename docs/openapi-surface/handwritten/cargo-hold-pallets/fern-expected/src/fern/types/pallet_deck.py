

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PalletDeck(enum.StrEnum):
    LOWER = "lower"
    MIDDLE = "middle"
    UPPER = "upper"

    def visit(
        self,
        lower: typing.Callable[[], T_Result],
        middle: typing.Callable[[], T_Result],
        upper: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PalletDeck.LOWER:
            return lower()
        if self is PalletDeck.MIDDLE:
            return middle()
        if self is PalletDeck.UPPER:
            return upper()
