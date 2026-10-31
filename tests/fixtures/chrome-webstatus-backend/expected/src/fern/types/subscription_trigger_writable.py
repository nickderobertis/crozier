

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SubscriptionTriggerWritable(enum.StrEnum):
    """
    The set of valid, user-selectable triggers for a subscription.
    """

    FEATURE_BASELINE_TO_NEWLY = "feature_baseline_to_newly"
    FEATURE_BASELINE_TO_WIDELY = "feature_baseline_to_widely"
    FEATURE_BROWSER_IMPLEMENTATION_ANY_COMPLETE = "feature_browser_implementation_any_complete"
    FEATURE_BASELINE_REGRESSION_TO_LIMITED = "feature_baseline_regression_to_limited"

    def visit(
        self,
        feature_baseline_to_newly: typing.Callable[[], T_Result],
        feature_baseline_to_widely: typing.Callable[[], T_Result],
        feature_browser_implementation_any_complete: typing.Callable[[], T_Result],
        feature_baseline_regression_to_limited: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SubscriptionTriggerWritable.FEATURE_BASELINE_TO_NEWLY:
            return feature_baseline_to_newly()
        if self is SubscriptionTriggerWritable.FEATURE_BASELINE_TO_WIDELY:
            return feature_baseline_to_widely()
        if self is SubscriptionTriggerWritable.FEATURE_BROWSER_IMPLEMENTATION_ANY_COMPLETE:
            return feature_browser_implementation_any_complete()
        if self is SubscriptionTriggerWritable.FEATURE_BASELINE_REGRESSION_TO_LIMITED:
            return feature_baseline_regression_to_limited()
