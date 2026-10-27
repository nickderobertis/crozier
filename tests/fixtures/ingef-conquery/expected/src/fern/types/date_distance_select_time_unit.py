

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DateDistanceSelectTimeUnit(enum.StrEnum):
    YEARS = "YEARS"
    DAYS = "DAYS"
    MONTHS = "MONTHS"
    WEEKS = "WEEKS"
    HOURS = "HOURS"

    def visit(
        self,
        years: typing.Callable[[], T_Result],
        days: typing.Callable[[], T_Result],
        months: typing.Callable[[], T_Result],
        weeks: typing.Callable[[], T_Result],
        hours: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DateDistanceSelectTimeUnit.YEARS:
            return years()
        if self is DateDistanceSelectTimeUnit.DAYS:
            return days()
        if self is DateDistanceSelectTimeUnit.MONTHS:
            return months()
        if self is DateDistanceSelectTimeUnit.WEEKS:
            return weeks()
        if self is DateDistanceSelectTimeUnit.HOURS:
            return hours()
