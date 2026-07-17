

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoyaltyProgramRewardDefinitionType(enum.StrEnum):
    """
    The type of discount the reward tier offers. DEPRECATED at version 2020-12-16. Discount details
    are now defined using a catalog pricing rule and other catalog objects. For more information, see
    [Get discount details for the reward](https://developer.squareup.com/docs/loyalty-api/overview#get-discount-details).
    """

    FIXED_AMOUNT = "FIXED_AMOUNT"
    FIXED_PERCENTAGE = "FIXED_PERCENTAGE"

    def visit(
        self, fixed_amount: typing.Callable[[], T_Result], fixed_percentage: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is LoyaltyProgramRewardDefinitionType.FIXED_AMOUNT:
            return fixed_amount()
        if self is LoyaltyProgramRewardDefinitionType.FIXED_PERCENTAGE:
            return fixed_percentage()
