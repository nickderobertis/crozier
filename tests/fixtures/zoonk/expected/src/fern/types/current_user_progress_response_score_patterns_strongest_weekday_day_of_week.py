

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CurrentUserProgressResponseScorePatternsStrongestWeekdayDayOfWeek(enum.StrEnum):
    SUNDAY = "sunday"
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"

    def visit(
        self,
        sunday: typing.Callable[[], T_Result],
        monday: typing.Callable[[], T_Result],
        tuesday: typing.Callable[[], T_Result],
        wednesday: typing.Callable[[], T_Result],
        thursday: typing.Callable[[], T_Result],
        friday: typing.Callable[[], T_Result],
        saturday: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CurrentUserProgressResponseScorePatternsStrongestWeekdayDayOfWeek.SUNDAY:
            return sunday()
        if self is CurrentUserProgressResponseScorePatternsStrongestWeekdayDayOfWeek.MONDAY:
            return monday()
        if self is CurrentUserProgressResponseScorePatternsStrongestWeekdayDayOfWeek.TUESDAY:
            return tuesday()
        if self is CurrentUserProgressResponseScorePatternsStrongestWeekdayDayOfWeek.WEDNESDAY:
            return wednesday()
        if self is CurrentUserProgressResponseScorePatternsStrongestWeekdayDayOfWeek.THURSDAY:
            return thursday()
        if self is CurrentUserProgressResponseScorePatternsStrongestWeekdayDayOfWeek.FRIDAY:
            return friday()
        if self is CurrentUserProgressResponseScorePatternsStrongestWeekdayDayOfWeek.SATURDAY:
            return saturday()
