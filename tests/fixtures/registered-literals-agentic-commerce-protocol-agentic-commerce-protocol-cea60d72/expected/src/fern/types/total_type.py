

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TotalType(enum.StrEnum):
    ITEMS_BASE_AMOUNT = "items_base_amount"
    ITEMS_DISCOUNT = "items_discount"
    SUBTOTAL = "subtotal"
    DISCOUNT = "discount"
    FULFILLMENT = "fulfillment"
    TAX = "tax"
    FEE = "fee"
    TOTAL = "total"

    def visit(
        self,
        items_base_amount: typing.Callable[[], T_Result],
        items_discount: typing.Callable[[], T_Result],
        subtotal: typing.Callable[[], T_Result],
        discount: typing.Callable[[], T_Result],
        fulfillment: typing.Callable[[], T_Result],
        tax: typing.Callable[[], T_Result],
        fee: typing.Callable[[], T_Result],
        total: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TotalType.ITEMS_BASE_AMOUNT:
            return items_base_amount()
        if self is TotalType.ITEMS_DISCOUNT:
            return items_discount()
        if self is TotalType.SUBTOTAL:
            return subtotal()
        if self is TotalType.DISCOUNT:
            return discount()
        if self is TotalType.FULFILLMENT:
            return fulfillment()
        if self is TotalType.TAX:
            return tax()
        if self is TotalType.FEE:
            return fee()
        if self is TotalType.TOTAL:
            return total()
