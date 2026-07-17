

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoyaltyProgramRewardDefinitionScope(enum.StrEnum):
    """
    Indicates the scope of the reward tier. DEPRECATED at version 2020-12-16. Discount details
    are now defined using a catalog pricing rule and other catalog objects. For more information, see
    [Get discount details for the reward](https://developer.squareup.com/docs/loyalty-api/overview#get-discount-details).
    """

    ORDER = "ORDER"
    ITEM_VARIATION = "ITEM_VARIATION"
    CATEGORY = "CATEGORY"

    def visit(
        self,
        order: typing.Callable[[], T_Result],
        item_variation: typing.Callable[[], T_Result],
        category: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LoyaltyProgramRewardDefinitionScope.ORDER:
            return order()
        if self is LoyaltyProgramRewardDefinitionScope.ITEM_VARIATION:
            return item_variation()
        if self is LoyaltyProgramRewardDefinitionScope.CATEGORY:
            return category()
