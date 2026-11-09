

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SubscriptionLimitDtoTimeIntervalBound(enum.StrEnum):
    """
    The time interval bound for the entitlement
    """

    SECONDS = "SECONDS"
    MINUTES = "MINUTES"
    HOURS = "HOURS"
    DAYS = "DAYS"

    def visit(
        self,
        seconds: typing.Callable[[], T_Result],
        minutes: typing.Callable[[], T_Result],
        hours: typing.Callable[[], T_Result],
        days: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SubscriptionLimitDtoTimeIntervalBound.SECONDS:
            return seconds()
        if self is SubscriptionLimitDtoTimeIntervalBound.MINUTES:
            return minutes()
        if self is SubscriptionLimitDtoTimeIntervalBound.HOURS:
            return hours()
        if self is SubscriptionLimitDtoTimeIntervalBound.DAYS:
            return days()
