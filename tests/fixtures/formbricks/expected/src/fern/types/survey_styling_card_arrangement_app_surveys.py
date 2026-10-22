

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyStylingCardArrangementAppSurveys(enum.StrEnum):
    CASUAL = "casual"
    STRAIGHT = "straight"
    SIMPLE = "simple"

    def visit(
        self,
        casual: typing.Callable[[], T_Result],
        straight: typing.Callable[[], T_Result],
        simple: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SurveyStylingCardArrangementAppSurveys.CASUAL:
            return casual()
        if self is SurveyStylingCardArrangementAppSurveys.STRAIGHT:
            return straight()
        if self is SurveyStylingCardArrangementAppSurveys.SIMPLE:
            return simple()
