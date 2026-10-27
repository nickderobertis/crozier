

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DateDistanceFilterTimeUnit(enum.StrEnum):
    YEARS = "YEARS"
    MONTHS = "MONTHS"
    DAYS = "DAYS"
    HOURS = "HOURS"

    def visit(
        self,
        years: typing.Callable[[], T_Result],
        months: typing.Callable[[], T_Result],
        days: typing.Callable[[], T_Result],
        hours: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DateDistanceFilterTimeUnit.YEARS:
            return years()
        if self is DateDistanceFilterTimeUnit.MONTHS:
            return months()
        if self is DateDistanceFilterTimeUnit.DAYS:
            return days()
        if self is DateDistanceFilterTimeUnit.HOURS:
            return hours()
