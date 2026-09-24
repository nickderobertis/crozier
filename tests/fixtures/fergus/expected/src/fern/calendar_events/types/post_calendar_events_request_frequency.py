

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostCalendarEventsRequestFrequency(enum.StrEnum):
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"
    YEARLY = "YEARLY"
    NEVER = "NEVER"

    def visit(
        self,
        daily: typing.Callable[[], T_Result],
        weekly: typing.Callable[[], T_Result],
        monthly: typing.Callable[[], T_Result],
        yearly: typing.Callable[[], T_Result],
        never: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostCalendarEventsRequestFrequency.DAILY:
            return daily()
        if self is PostCalendarEventsRequestFrequency.WEEKLY:
            return weekly()
        if self is PostCalendarEventsRequestFrequency.MONTHLY:
            return monthly()
        if self is PostCalendarEventsRequestFrequency.YEARLY:
            return yearly()
        if self is PostCalendarEventsRequestFrequency.NEVER:
            return never()
