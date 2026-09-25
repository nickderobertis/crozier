

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostCalendarEventsCalendarEventIdRequestFrequency(enum.StrEnum):
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
        if self is PostCalendarEventsCalendarEventIdRequestFrequency.DAILY:
            return daily()
        if self is PostCalendarEventsCalendarEventIdRequestFrequency.WEEKLY:
            return weekly()
        if self is PostCalendarEventsCalendarEventIdRequestFrequency.MONTHLY:
            return monthly()
        if self is PostCalendarEventsCalendarEventIdRequestFrequency.YEARLY:
            return yearly()
        if self is PostCalendarEventsCalendarEventIdRequestFrequency.NEVER:
            return never()
