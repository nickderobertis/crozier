

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostCalendarEventsRequestEventType(enum.StrEnum):
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
        if self is PostCalendarEventsRequestEventType.JOB_PHASE:
            return job_phase()
        if self is PostCalendarEventsRequestEventType.QUOTE:
            return quote()
        if self is PostCalendarEventsRequestEventType.ESTIMATE:
            return estimate()
        if self is PostCalendarEventsRequestEventType.OTHER:
            return other()
