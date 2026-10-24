

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BriefingMetricTrendMode(enum.StrEnum):
    HIGHER_IS_BETTER = "higher_is_better"
    HIGHER_IS_RISK = "higher_is_risk"
    CONTEXT_ONLY = "context_only"

    def visit(
        self,
        higher_is_better: typing.Callable[[], T_Result],
        higher_is_risk: typing.Callable[[], T_Result],
        context_only: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BriefingMetricTrendMode.HIGHER_IS_BETTER:
            return higher_is_better()
        if self is BriefingMetricTrendMode.HIGHER_IS_RISK:
            return higher_is_risk()
        if self is BriefingMetricTrendMode.CONTEXT_ONLY:
            return context_only()
