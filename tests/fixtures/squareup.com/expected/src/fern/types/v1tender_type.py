

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class V1TenderType(str, enum.Enum):
    """ """

    CREDIT_CARD = "CREDIT_CARD"
    CASH = "CASH"
    THIRD_PARTY_CARD = "THIRD_PARTY_CARD"
    NO_SALE = "NO_SALE"
    SQUARE_WALLET = "SQUARE_WALLET"
    SQUARE_GIFT_CARD = "SQUARE_GIFT_CARD"
    UNKNOWN = "UNKNOWN"
    OTHER = "OTHER"

    def visit(
        self,
        credit_card: typing.Callable[[], T_Result],
        cash: typing.Callable[[], T_Result],
        third_party_card: typing.Callable[[], T_Result],
        no_sale: typing.Callable[[], T_Result],
        square_wallet: typing.Callable[[], T_Result],
        square_gift_card: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1TenderType.CREDIT_CARD:
            return credit_card()
        if self is V1TenderType.CASH:
            return cash()
        if self is V1TenderType.THIRD_PARTY_CARD:
            return third_party_card()
        if self is V1TenderType.NO_SALE:
            return no_sale()
        if self is V1TenderType.SQUARE_WALLET:
            return square_wallet()
        if self is V1TenderType.SQUARE_GIFT_CARD:
            return square_gift_card()
        if self is V1TenderType.UNKNOWN:
            return unknown()
        if self is V1TenderType.OTHER:
            return other()
