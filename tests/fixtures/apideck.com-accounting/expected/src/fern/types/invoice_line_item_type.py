

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InvoiceLineItemType(enum.StrEnum):
    """
    Item type
    """

    SALES_ITEM = "sales_item"
    DISCOUNT = "discount"
    INFO = "info"
    SUB_TOTAL = "sub_total"

    def visit(
        self,
        sales_item: typing.Callable[[], T_Result],
        discount: typing.Callable[[], T_Result],
        info: typing.Callable[[], T_Result],
        sub_total: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InvoiceLineItemType.SALES_ITEM:
            return sales_item()
        if self is InvoiceLineItemType.DISCOUNT:
            return discount()
        if self is InvoiceLineItemType.INFO:
            return info()
        if self is InvoiceLineItemType.SUB_TOTAL:
            return sub_total()
