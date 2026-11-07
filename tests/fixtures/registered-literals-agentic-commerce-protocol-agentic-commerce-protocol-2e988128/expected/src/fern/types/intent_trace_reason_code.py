

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IntentTraceReasonCode(enum.StrEnum):
    """
    Reason for abandonment. This enum is extensible: servers SHOULD accept
    unrecognized values and treat them as "other" (see RFC Section 7.2).
    Validators SHOULD be configured for lenient enum handling.
    """

    PRICE_SENSITIVITY = "price_sensitivity"
    SHIPPING_COST = "shipping_cost"
    SHIPPING_SPEED = "shipping_speed"
    PRODUCT_FIT = "product_fit"
    TRUST_SECURITY = "trust_security"
    RETURNS_POLICY = "returns_policy"
    PAYMENT_OPTIONS = "payment_options"
    COMPARISON = "comparison"
    TIMING_DEFERRED = "timing_deferred"
    OTHER = "other"

    def visit(
        self,
        price_sensitivity: typing.Callable[[], T_Result],
        shipping_cost: typing.Callable[[], T_Result],
        shipping_speed: typing.Callable[[], T_Result],
        product_fit: typing.Callable[[], T_Result],
        trust_security: typing.Callable[[], T_Result],
        returns_policy: typing.Callable[[], T_Result],
        payment_options: typing.Callable[[], T_Result],
        comparison: typing.Callable[[], T_Result],
        timing_deferred: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IntentTraceReasonCode.PRICE_SENSITIVITY:
            return price_sensitivity()
        if self is IntentTraceReasonCode.SHIPPING_COST:
            return shipping_cost()
        if self is IntentTraceReasonCode.SHIPPING_SPEED:
            return shipping_speed()
        if self is IntentTraceReasonCode.PRODUCT_FIT:
            return product_fit()
        if self is IntentTraceReasonCode.TRUST_SECURITY:
            return trust_security()
        if self is IntentTraceReasonCode.RETURNS_POLICY:
            return returns_policy()
        if self is IntentTraceReasonCode.PAYMENT_OPTIONS:
            return payment_options()
        if self is IntentTraceReasonCode.COMPARISON:
            return comparison()
        if self is IntentTraceReasonCode.TIMING_DEFERRED:
            return timing_deferred()
        if self is IntentTraceReasonCode.OTHER:
            return other()
