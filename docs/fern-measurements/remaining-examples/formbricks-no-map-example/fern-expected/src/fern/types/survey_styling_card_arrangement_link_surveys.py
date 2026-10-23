

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyStylingCardArrangementLinkSurveys(enum.StrEnum):
    CASUAL = "casual"
    STRAIGHT = "straight"
    SIMPLE = "simple"

    def visit(
        self,
        casual: typing.Callable[[], T_Result],
        straight: typing.Callable[[], T_Result],
        simple: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SurveyStylingCardArrangementLinkSurveys.CASUAL:
            return casual()
        if self is SurveyStylingCardArrangementLinkSurveys.STRAIGHT:
            return straight()
        if self is SurveyStylingCardArrangementLinkSurveys.SIMPLE:
            return simple()
