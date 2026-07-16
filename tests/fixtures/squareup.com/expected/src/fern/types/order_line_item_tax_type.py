

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OrderLineItemTaxType(str, enum.Enum):
    """
    Indicates how the tax is applied to the associated line item or order.
    """

    UNKNOWN_TAX = "UNKNOWN_TAX"
    ADDITIVE = "ADDITIVE"
    INCLUSIVE = "INCLUSIVE"

    def visit(
        self,
        unknown_tax: typing.Callable[[], T_Result],
        additive: typing.Callable[[], T_Result],
        inclusive: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OrderLineItemTaxType.UNKNOWN_TAX:
            return unknown_tax()
        if self is OrderLineItemTaxType.ADDITIVE:
            return additive()
        if self is OrderLineItemTaxType.INCLUSIVE:
            return inclusive()
