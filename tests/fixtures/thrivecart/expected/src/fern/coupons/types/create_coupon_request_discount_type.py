

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateCouponRequestDiscountType(enum.StrEnum):
    PERCENTAGE = "percentage"
    FIXED = "fixed"

    def visit(self, percentage: typing.Callable[[], T_Result], fixed: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateCouponRequestDiscountType.PERCENTAGE:
            return percentage()
        if self is CreateCouponRequestDiscountType.FIXED:
            return fixed()
