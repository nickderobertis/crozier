

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObReadOffer1DataOfferItemOfferType(enum.StrEnum):
    """
    Offer type, in a coded form.
    """

    BALANCE_TRANSFER = "BalanceTransfer"
    LIMIT_INCREASE = "LimitIncrease"
    MONEY_TRANSFER = "MoneyTransfer"
    OTHER = "Other"
    PROMOTIONAL_RATE = "PromotionalRate"

    def visit(
        self,
        balance_transfer: typing.Callable[[], T_Result],
        limit_increase: typing.Callable[[], T_Result],
        money_transfer: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        promotional_rate: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObReadOffer1DataOfferItemOfferType.BALANCE_TRANSFER:
            return balance_transfer()
        if self is ObReadOffer1DataOfferItemOfferType.LIMIT_INCREASE:
            return limit_increase()
        if self is ObReadOffer1DataOfferItemOfferType.MONEY_TRANSFER:
            return money_transfer()
        if self is ObReadOffer1DataOfferItemOfferType.OTHER:
            return other()
        if self is ObReadOffer1DataOfferItemOfferType.PROMOTIONAL_RATE:
            return promotional_rate()
