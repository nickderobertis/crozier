

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GiftCardActivityAdjustDecrementReason(enum.StrEnum):
    """ """

    SUSPICIOUS_ACTIVITY = "SUSPICIOUS_ACTIVITY"
    BALANCE_ACCIDENTALLY_INCREASED = "BALANCE_ACCIDENTALLY_INCREASED"
    SUPPORT_ISSUE = "SUPPORT_ISSUE"

    def visit(
        self,
        suspicious_activity: typing.Callable[[], T_Result],
        balance_accidentally_increased: typing.Callable[[], T_Result],
        support_issue: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GiftCardActivityAdjustDecrementReason.SUSPICIOUS_ACTIVITY:
            return suspicious_activity()
        if self is GiftCardActivityAdjustDecrementReason.BALANCE_ACCIDENTALLY_INCREASED:
            return balance_accidentally_increased()
        if self is GiftCardActivityAdjustDecrementReason.SUPPORT_ISSUE:
            return support_issue()
