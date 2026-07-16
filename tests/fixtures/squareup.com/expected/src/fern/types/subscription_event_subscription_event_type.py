

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class SubscriptionEventSubscriptionEventType(str, enum.Enum):
    """
    The possible subscription event types.
    """

    START_SUBSCRIPTION = "START_SUBSCRIPTION"
    PLAN_CHANGE = "PLAN_CHANGE"
    STOP_SUBSCRIPTION = "STOP_SUBSCRIPTION"
    DEACTIVATE_SUBSCRIPTION = "DEACTIVATE_SUBSCRIPTION"
    RESUME_SUBSCRIPTION = "RESUME_SUBSCRIPTION"

    def visit(
        self,
        start_subscription: typing.Callable[[], T_Result],
        plan_change: typing.Callable[[], T_Result],
        stop_subscription: typing.Callable[[], T_Result],
        deactivate_subscription: typing.Callable[[], T_Result],
        resume_subscription: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SubscriptionEventSubscriptionEventType.START_SUBSCRIPTION:
            return start_subscription()
        if self is SubscriptionEventSubscriptionEventType.PLAN_CHANGE:
            return plan_change()
        if self is SubscriptionEventSubscriptionEventType.STOP_SUBSCRIPTION:
            return stop_subscription()
        if self is SubscriptionEventSubscriptionEventType.DEACTIVATE_SUBSCRIPTION:
            return deactivate_subscription()
        if self is SubscriptionEventSubscriptionEventType.RESUME_SUBSCRIPTION:
            return resume_subscription()
