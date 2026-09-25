

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserSubscriptionPlan(enum.StrEnum):
    FREE = "FREE"
    PRO = "PRO"
    BUSINESS = "BUSINESS"

    def visit(
        self,
        free: typing.Callable[[], T_Result],
        pro: typing.Callable[[], T_Result],
        business: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UserSubscriptionPlan.FREE:
            return free()
        if self is UserSubscriptionPlan.PRO:
            return pro()
        if self is UserSubscriptionPlan.BUSINESS:
            return business()
