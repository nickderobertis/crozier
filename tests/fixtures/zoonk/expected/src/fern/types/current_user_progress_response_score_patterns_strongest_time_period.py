

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CurrentUserProgressResponseScorePatternsStrongestTimePeriod(enum.StrEnum):
    NIGHT = "night"
    MORNING = "morning"
    AFTERNOON = "afternoon"
    EVENING = "evening"

    def visit(
        self,
        night: typing.Callable[[], T_Result],
        morning: typing.Callable[[], T_Result],
        afternoon: typing.Callable[[], T_Result],
        evening: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CurrentUserProgressResponseScorePatternsStrongestTimePeriod.NIGHT:
            return night()
        if self is CurrentUserProgressResponseScorePatternsStrongestTimePeriod.MORNING:
            return morning()
        if self is CurrentUserProgressResponseScorePatternsStrongestTimePeriod.AFTERNOON:
            return afternoon()
        if self is CurrentUserProgressResponseScorePatternsStrongestTimePeriod.EVENING:
            return evening()
