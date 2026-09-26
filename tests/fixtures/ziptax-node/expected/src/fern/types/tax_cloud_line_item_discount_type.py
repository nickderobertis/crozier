

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TaxCloudLineItemDiscountType(enum.StrEnum):
    """
    The kind of discount: 'percentage' (a fraction of the price) or 'amount' (a fixed currency amount).
    """

    PERCENTAGE = "percentage"
    AMOUNT = "amount"

    def visit(self, percentage: typing.Callable[[], T_Result], amount: typing.Callable[[], T_Result]) -> T_Result:
        if self is TaxCloudLineItemDiscountType.PERCENTAGE:
            return percentage()
        if self is TaxCloudLineItemDiscountType.AMOUNT:
            return amount()
