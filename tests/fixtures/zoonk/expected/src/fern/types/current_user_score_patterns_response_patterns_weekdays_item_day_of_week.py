

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CurrentUserScorePatternsResponsePatternsWeekdaysItemDayOfWeek(enum.StrEnum):
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
        if self is CurrentUserScorePatternsResponsePatternsWeekdaysItemDayOfWeek.SUNDAY:
            return sunday()
        if self is CurrentUserScorePatternsResponsePatternsWeekdaysItemDayOfWeek.MONDAY:
            return monday()
        if self is CurrentUserScorePatternsResponsePatternsWeekdaysItemDayOfWeek.TUESDAY:
            return tuesday()
        if self is CurrentUserScorePatternsResponsePatternsWeekdaysItemDayOfWeek.WEDNESDAY:
            return wednesday()
        if self is CurrentUserScorePatternsResponsePatternsWeekdaysItemDayOfWeek.THURSDAY:
            return thursday()
        if self is CurrentUserScorePatternsResponsePatternsWeekdaysItemDayOfWeek.FRIDAY:
            return friday()
        if self is CurrentUserScorePatternsResponsePatternsWeekdaysItemDayOfWeek.SATURDAY:
            return saturday()
