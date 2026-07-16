

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GiftCardActivityClearBalanceReason(str, enum.Enum):
    """ """

    SUSPICIOUS_ACTIVITY = "SUSPICIOUS_ACTIVITY"
    REUSE_GIFTCARD = "REUSE_GIFTCARD"
    UNKNOWN_REASON = "UNKNOWN_REASON"

    def visit(
        self,
        suspicious_activity: typing.Callable[[], T_Result],
        reuse_giftcard: typing.Callable[[], T_Result],
        unknown_reason: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GiftCardActivityClearBalanceReason.SUSPICIOUS_ACTIVITY:
            return suspicious_activity()
        if self is GiftCardActivityClearBalanceReason.REUSE_GIFTCARD:
            return reuse_giftcard()
        if self is GiftCardActivityClearBalanceReason.UNKNOWN_REASON:
            return unknown_reason()
