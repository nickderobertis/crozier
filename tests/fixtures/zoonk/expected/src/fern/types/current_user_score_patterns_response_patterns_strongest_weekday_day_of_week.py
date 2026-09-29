

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CurrentUserScorePatternsResponsePatternsStrongestWeekdayDayOfWeek(enum.StrEnum):
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
        if self is CurrentUserScorePatternsResponsePatternsStrongestWeekdayDayOfWeek.SUNDAY:
            return sunday()
        if self is CurrentUserScorePatternsResponsePatternsStrongestWeekdayDayOfWeek.MONDAY:
            return monday()
        if self is CurrentUserScorePatternsResponsePatternsStrongestWeekdayDayOfWeek.TUESDAY:
            return tuesday()
        if self is CurrentUserScorePatternsResponsePatternsStrongestWeekdayDayOfWeek.WEDNESDAY:
            return wednesday()
        if self is CurrentUserScorePatternsResponsePatternsStrongestWeekdayDayOfWeek.THURSDAY:
            return thursday()
        if self is CurrentUserScorePatternsResponsePatternsStrongestWeekdayDayOfWeek.FRIDAY:
            return friday()
        if self is CurrentUserScorePatternsResponsePatternsStrongestWeekdayDayOfWeek.SATURDAY:
            return saturday()
