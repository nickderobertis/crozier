

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OrderLineItemTaxScope(enum.StrEnum):
    """
    Indicates whether this is a line-item or order-level tax.
    """

    OTHER_TAX_SCOPE = "OTHER_TAX_SCOPE"
    LINE_ITEM = "LINE_ITEM"
    ORDER = "ORDER"

    def visit(
        self,
        other_tax_scope: typing.Callable[[], T_Result],
        line_item: typing.Callable[[], T_Result],
        order: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OrderLineItemTaxScope.OTHER_TAX_SCOPE:
            return other_tax_scope()
        if self is OrderLineItemTaxScope.LINE_ITEM:
            return line_item()
        if self is OrderLineItemTaxScope.ORDER:
            return order()
