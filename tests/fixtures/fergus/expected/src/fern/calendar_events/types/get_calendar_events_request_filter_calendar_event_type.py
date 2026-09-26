

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetCalendarEventsRequestFilterCalendarEventType(enum.StrEnum):
    JOB_PHASE = "JOB_PHASE"
    QUOTE = "QUOTE"
    ESTIMATE = "ESTIMATE"
    OTHER = "OTHER"

    def visit(
        self,
        job_phase: typing.Callable[[], T_Result],
        quote: typing.Callable[[], T_Result],
        estimate: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetCalendarEventsRequestFilterCalendarEventType.JOB_PHASE:
            return job_phase()
        if self is GetCalendarEventsRequestFilterCalendarEventType.QUOTE:
            return quote()
        if self is GetCalendarEventsRequestFilterCalendarEventType.ESTIMATE:
            return estimate()
        if self is GetCalendarEventsRequestFilterCalendarEventType.OTHER:
            return other()
