

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SubscriptionFrequency(enum.StrEnum):
    """
    The frequency for a subscription.
    """

    IMMEDIATE = "immediate"
    WEEKLY = "weekly"
    MONTHLY = "monthly"

    def visit(
        self,
        immediate: typing.Callable[[], T_Result],
        weekly: typing.Callable[[], T_Result],
        monthly: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SubscriptionFrequency.IMMEDIATE:
            return immediate()
        if self is SubscriptionFrequency.WEEKLY:
            return weekly()
        if self is SubscriptionFrequency.MONTHLY:
            return monthly()
