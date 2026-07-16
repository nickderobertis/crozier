

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GiftCardActivityDeactivateReason(str, enum.Enum):
    """ """

    SUSPICIOUS_ACTIVITY = "SUSPICIOUS_ACTIVITY"
    UNKNOWN_REASON = "UNKNOWN_REASON"
    CHARGEBACK_DEACTIVATE = "CHARGEBACK_DEACTIVATE"

    def visit(
        self,
        suspicious_activity: typing.Callable[[], T_Result],
        unknown_reason: typing.Callable[[], T_Result],
        chargeback_deactivate: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GiftCardActivityDeactivateReason.SUSPICIOUS_ACTIVITY:
            return suspicious_activity()
        if self is GiftCardActivityDeactivateReason.UNKNOWN_REASON:
            return unknown_reason()
        if self is GiftCardActivityDeactivateReason.CHARGEBACK_DEACTIVATE:
            return chargeback_deactivate()
