

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SettlementDelayLiftedNotificationResourceReason(enum.StrEnum):
    """
    The reason for the change in your account holder's settlement delay.

    Possible values: **paymentProcessingEnabled**, **settlementDelayChanged**, **riskReviewPeriodPassed**.
    """

    PAYMENT_PROCESSING_ENABLED = "paymentProcessingEnabled"
    SETTLEMENT_DELAY_CHANGED = "settlementDelayChanged"
    RISK_REVIEW_PERIOD_PASSED = "riskReviewPeriodPassed"

    def visit(
        self,
        payment_processing_enabled: typing.Callable[[], T_Result],
        settlement_delay_changed: typing.Callable[[], T_Result],
        risk_review_period_passed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SettlementDelayLiftedNotificationResourceReason.PAYMENT_PROCESSING_ENABLED:
            return payment_processing_enabled()
        if self is SettlementDelayLiftedNotificationResourceReason.SETTLEMENT_DELAY_CHANGED:
            return settlement_delay_changed()
        if self is SettlementDelayLiftedNotificationResourceReason.RISK_REVIEW_PERIOD_PASSED:
            return risk_review_period_passed()
