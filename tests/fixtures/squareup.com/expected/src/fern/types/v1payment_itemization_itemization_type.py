

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1PaymentItemizationItemizationType(enum.StrEnum):
    """ """

    ITEM = "ITEM"
    CUSTOM_AMOUNT = "CUSTOM_AMOUNT"
    GIFT_CARD_ACTIVATION = "GIFT_CARD_ACTIVATION"
    GIFT_CARD_RELOAD = "GIFT_CARD_RELOAD"
    GIFT_CARD_UNKNOWN = "GIFT_CARD_UNKNOWN"
    OTHER = "OTHER"

    def visit(
        self,
        item: typing.Callable[[], T_Result],
        custom_amount: typing.Callable[[], T_Result],
        gift_card_activation: typing.Callable[[], T_Result],
        gift_card_reload: typing.Callable[[], T_Result],
        gift_card_unknown: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1PaymentItemizationItemizationType.ITEM:
            return item()
        if self is V1PaymentItemizationItemizationType.CUSTOM_AMOUNT:
            return custom_amount()
        if self is V1PaymentItemizationItemizationType.GIFT_CARD_ACTIVATION:
            return gift_card_activation()
        if self is V1PaymentItemizationItemizationType.GIFT_CARD_RELOAD:
            return gift_card_reload()
        if self is V1PaymentItemizationItemizationType.GIFT_CARD_UNKNOWN:
            return gift_card_unknown()
        if self is V1PaymentItemizationItemizationType.OTHER:
            return other()
