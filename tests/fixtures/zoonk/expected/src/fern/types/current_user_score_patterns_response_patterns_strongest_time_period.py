

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CurrentUserScorePatternsResponsePatternsStrongestTimePeriod(enum.StrEnum):
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
        if self is CurrentUserScorePatternsResponsePatternsStrongestTimePeriod.NIGHT:
            return night()
        if self is CurrentUserScorePatternsResponsePatternsStrongestTimePeriod.MORNING:
            return morning()
        if self is CurrentUserScorePatternsResponsePatternsStrongestTimePeriod.AFTERNOON:
            return afternoon()
        if self is CurrentUserScorePatternsResponsePatternsStrongestTimePeriod.EVENING:
            return evening()
