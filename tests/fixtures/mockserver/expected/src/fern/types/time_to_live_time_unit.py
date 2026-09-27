

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TimeToLiveTimeUnit(enum.StrEnum):
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
        if self is TimeToLiveTimeUnit.DAYS:
            return days()
        if self is TimeToLiveTimeUnit.HOURS:
            return hours()
        if self is TimeToLiveTimeUnit.MINUTES:
            return minutes()
        if self is TimeToLiveTimeUnit.SECONDS:
            return seconds()
        if self is TimeToLiveTimeUnit.MILLISECONDS:
            return milliseconds()
        if self is TimeToLiveTimeUnit.MICROSECONDS:
            return microseconds()
        if self is TimeToLiveTimeUnit.NANOSECONDS:
            return nanoseconds()
