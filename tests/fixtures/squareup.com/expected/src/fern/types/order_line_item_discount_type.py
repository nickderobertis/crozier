

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OrderLineItemDiscountType(enum.StrEnum):
    """
    Indicates how the discount is applied to the associated line item or order.
    """

    UNKNOWN_DISCOUNT = "UNKNOWN_DISCOUNT"
    FIXED_PERCENTAGE = "FIXED_PERCENTAGE"
    FIXED_AMOUNT = "FIXED_AMOUNT"
    VARIABLE_PERCENTAGE = "VARIABLE_PERCENTAGE"
    VARIABLE_AMOUNT = "VARIABLE_AMOUNT"

    def visit(
        self,
        unknown_discount: typing.Callable[[], T_Result],
        fixed_percentage: typing.Callable[[], T_Result],
        fixed_amount: typing.Callable[[], T_Result],
        variable_percentage: typing.Callable[[], T_Result],
        variable_amount: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OrderLineItemDiscountType.UNKNOWN_DISCOUNT:
            return unknown_discount()
        if self is OrderLineItemDiscountType.FIXED_PERCENTAGE:
            return fixed_percentage()
        if self is OrderLineItemDiscountType.FIXED_AMOUNT:
            return fixed_amount()
        if self is OrderLineItemDiscountType.VARIABLE_PERCENTAGE:
            return variable_percentage()
        if self is OrderLineItemDiscountType.VARIABLE_AMOUNT:
            return variable_amount()
