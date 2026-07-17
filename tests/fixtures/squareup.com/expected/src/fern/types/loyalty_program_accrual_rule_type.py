

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoyaltyProgramAccrualRuleType(enum.StrEnum):
    """
    The type of the accrual rule that defines how buyers can earn points.
    """

    VISIT = "VISIT"
    SPEND = "SPEND"
    ITEM_VARIATION = "ITEM_VARIATION"
    CATEGORY = "CATEGORY"

    def visit(
        self,
        visit: typing.Callable[[], T_Result],
        spend: typing.Callable[[], T_Result],
        item_variation: typing.Callable[[], T_Result],
        category: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LoyaltyProgramAccrualRuleType.VISIT:
            return visit()
        if self is LoyaltyProgramAccrualRuleType.SPEND:
            return spend()
        if self is LoyaltyProgramAccrualRuleType.ITEM_VARIATION:
            return item_variation()
        if self is LoyaltyProgramAccrualRuleType.CATEGORY:
            return category()
