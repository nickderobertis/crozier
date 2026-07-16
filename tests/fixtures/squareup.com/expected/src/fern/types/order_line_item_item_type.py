

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OrderLineItemItemType(str, enum.Enum):
    """
    Represents the line item type.
    """

    ITEM = "ITEM"
    CUSTOM_AMOUNT = "CUSTOM_AMOUNT"
    GIFT_CARD = "GIFT_CARD"

    def visit(
        self,
        item: typing.Callable[[], T_Result],
        custom_amount: typing.Callable[[], T_Result],
        gift_card: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OrderLineItemItemType.ITEM:
            return item()
        if self is OrderLineItemItemType.CUSTOM_AMOUNT:
            return custom_amount()
        if self is OrderLineItemItemType.GIFT_CARD:
            return gift_card()
