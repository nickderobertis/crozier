

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TenderType(enum.StrEnum):
    """
    Indicates a tender's type.
    """

    CARD = "CARD"
    CASH = "CASH"
    THIRD_PARTY_CARD = "THIRD_PARTY_CARD"
    SQUARE_GIFT_CARD = "SQUARE_GIFT_CARD"
    NO_SALE = "NO_SALE"
    WALLET = "WALLET"
    OTHER = "OTHER"

    def visit(
        self,
        card: typing.Callable[[], T_Result],
        cash: typing.Callable[[], T_Result],
        third_party_card: typing.Callable[[], T_Result],
        square_gift_card: typing.Callable[[], T_Result],
        no_sale: typing.Callable[[], T_Result],
        wallet: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TenderType.CARD:
            return card()
        if self is TenderType.CASH:
            return cash()
        if self is TenderType.THIRD_PARTY_CARD:
            return third_party_card()
        if self is TenderType.SQUARE_GIFT_CARD:
            return square_gift_card()
        if self is TenderType.NO_SALE:
            return no_sale()
        if self is TenderType.WALLET:
            return wallet()
        if self is TenderType.OTHER:
            return other()
