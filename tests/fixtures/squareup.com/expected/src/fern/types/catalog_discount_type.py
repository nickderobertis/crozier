

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CatalogDiscountType(enum.StrEnum):
    """
    How to apply a CatalogDiscount to a CatalogItem.
    """

    FIXED_PERCENTAGE = "FIXED_PERCENTAGE"
    FIXED_AMOUNT = "FIXED_AMOUNT"
    VARIABLE_PERCENTAGE = "VARIABLE_PERCENTAGE"
    VARIABLE_AMOUNT = "VARIABLE_AMOUNT"

    def visit(
        self,
        fixed_percentage: typing.Callable[[], T_Result],
        fixed_amount: typing.Callable[[], T_Result],
        variable_percentage: typing.Callable[[], T_Result],
        variable_amount: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CatalogDiscountType.FIXED_PERCENTAGE:
            return fixed_percentage()
        if self is CatalogDiscountType.FIXED_AMOUNT:
            return fixed_amount()
        if self is CatalogDiscountType.VARIABLE_PERCENTAGE:
            return variable_percentage()
        if self is CatalogDiscountType.VARIABLE_AMOUNT:
            return variable_amount()
