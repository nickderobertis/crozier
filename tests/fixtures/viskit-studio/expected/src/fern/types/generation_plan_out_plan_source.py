

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GenerationPlanOutPlanSource(enum.StrEnum):
    EXPLICIT = "explicit"
    RECOMMENDED = "recommended"
    FALLBACK = "fallback"
    MANUAL = "manual"

    def visit(
        self,
        explicit: typing.Callable[[], T_Result],
        recommended: typing.Callable[[], T_Result],
        fallback: typing.Callable[[], T_Result],
        manual: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GenerationPlanOutPlanSource.EXPLICIT:
            return explicit()
        if self is GenerationPlanOutPlanSource.RECOMMENDED:
            return recommended()
        if self is GenerationPlanOutPlanSource.FALLBACK:
            return fallback()
        if self is GenerationPlanOutPlanSource.MANUAL:
            return manual()
