

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoyaltyRewardStatus(enum.StrEnum):
    """
    The status of the loyalty reward.
    """

    ISSUED = "ISSUED"
    REDEEMED = "REDEEMED"
    DELETED = "DELETED"

    def visit(
        self,
        issued: typing.Callable[[], T_Result],
        redeemed: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LoyaltyRewardStatus.ISSUED:
            return issued()
        if self is LoyaltyRewardStatus.REDEEMED:
            return redeemed()
        if self is LoyaltyRewardStatus.DELETED:
            return deleted()
