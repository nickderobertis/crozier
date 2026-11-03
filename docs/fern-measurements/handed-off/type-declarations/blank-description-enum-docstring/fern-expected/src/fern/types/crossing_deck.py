

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CrossingDeck(enum.StrEnum):
    """ """

    UPPER = "UPPER"
    LOWER = "LOWER"

    def visit(self, upper: typing.Callable[[], T_Result], lower: typing.Callable[[], T_Result]) -> T_Result:
        if self is CrossingDeck.UPPER:
            return upper()
        if self is CrossingDeck.LOWER:
            return lower()
