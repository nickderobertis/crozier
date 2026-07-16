

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OrderLineItemDiscountScope(str, enum.Enum):
    """
    Indicates whether this is a line-item or order-level discount.
    """

    OTHER_DISCOUNT_SCOPE = "OTHER_DISCOUNT_SCOPE"
    LINE_ITEM = "LINE_ITEM"
    ORDER = "ORDER"

    def visit(
        self,
        other_discount_scope: typing.Callable[[], T_Result],
        line_item: typing.Callable[[], T_Result],
        order: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OrderLineItemDiscountScope.OTHER_DISCOUNT_SCOPE:
            return other_discount_scope()
        if self is OrderLineItemDiscountScope.LINE_ITEM:
            return line_item()
        if self is OrderLineItemDiscountScope.ORDER:
            return order()
