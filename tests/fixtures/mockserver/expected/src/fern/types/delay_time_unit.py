

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DelayTimeUnit(enum.StrEnum):
    DAYS = "DAYS"
    HOURS = "HOURS"
    MINUTES = "MINUTES"
    SECONDS = "SECONDS"
    MILLISECONDS = "MILLISECONDS"
    MICROSECONDS = "MICROSECONDS"
    NANOSECONDS = "NANOSECONDS"

    def visit(
        self,
        days: typing.Callable[[], T_Result],
        hours: typing.Callable[[], T_Result],
        minutes: typing.Callable[[], T_Result],
        seconds: typing.Callable[[], T_Result],
        milliseconds: typing.Callable[[], T_Result],
        microseconds: typing.Callable[[], T_Result],
        nanoseconds: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DelayTimeUnit.DAYS:
            return days()
        if self is DelayTimeUnit.HOURS:
            return hours()
        if self is DelayTimeUnit.MINUTES:
            return minutes()
        if self is DelayTimeUnit.SECONDS:
            return seconds()
        if self is DelayTimeUnit.MILLISECONDS:
            return milliseconds()
        if self is DelayTimeUnit.MICROSECONDS:
            return microseconds()
        if self is DelayTimeUnit.NANOSECONDS:
            return nanoseconds()
