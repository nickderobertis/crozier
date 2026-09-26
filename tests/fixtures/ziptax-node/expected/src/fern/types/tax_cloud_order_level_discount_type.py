

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TaxCloudOrderLevelDiscountType(enum.StrEnum):
    """
    The kind of discount: 'percentage' (a fraction of the order total) or 'amount' (a fixed currency amount).
    """

    PERCENTAGE = "percentage"
    AMOUNT = "amount"

    def visit(self, percentage: typing.Callable[[], T_Result], amount: typing.Callable[[], T_Result]) -> T_Result:
        if self is TaxCloudOrderLevelDiscountType.PERCENTAGE:
            return percentage()
        if self is TaxCloudOrderLevelDiscountType.AMOUNT:
            return amount()
