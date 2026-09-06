

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateFulfillOrdersResponseTotalsExtrasItemType(enum.StrEnum):
    """
    The type of extra item this is.
    """

    DISCOUNT = "discount"
    DISCOUNT_SHIPPING = "discount-shipping"
    SHIPPING = "shipping"
    TAX = "tax"

    def visit(
        self,
        discount: typing.Callable[[], T_Result],
        discount_shipping: typing.Callable[[], T_Result],
        shipping: typing.Callable[[], T_Result],
        tax: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdateFulfillOrdersResponseTotalsExtrasItemType.DISCOUNT:
            return discount()
        if self is UpdateFulfillOrdersResponseTotalsExtrasItemType.DISCOUNT_SHIPPING:
            return discount_shipping()
        if self is UpdateFulfillOrdersResponseTotalsExtrasItemType.SHIPPING:
            return shipping()
        if self is UpdateFulfillOrdersResponseTotalsExtrasItemType.TAX:
            return tax()
