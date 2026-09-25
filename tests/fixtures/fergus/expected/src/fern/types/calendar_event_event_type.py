

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CalendarEventEventType(enum.StrEnum):
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
        if self is CalendarEventEventType.JOB_PHASE:
            return job_phase()
        if self is CalendarEventEventType.QUOTE:
            return quote()
        if self is CalendarEventEventType.ESTIMATE:
            return estimate()
        if self is CalendarEventEventType.OTHER:
            return other()
