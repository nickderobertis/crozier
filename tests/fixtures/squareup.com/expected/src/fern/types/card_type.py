

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CardType(enum.StrEnum):
    """
    Indicates a card's type, such as `CREDIT` or `DEBIT`.
    """

    UNKNOWN_CARD_TYPE = "UNKNOWN_CARD_TYPE"
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"

    def visit(
        self,
        unknown_card_type: typing.Callable[[], T_Result],
        credit: typing.Callable[[], T_Result],
        debit: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CardType.UNKNOWN_CARD_TYPE:
            return unknown_card_type()
        if self is CardType.CREDIT:
            return credit()
        if self is CardType.DEBIT:
            return debit()
