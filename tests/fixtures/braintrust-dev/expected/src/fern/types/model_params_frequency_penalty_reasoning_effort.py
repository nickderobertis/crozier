

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelParamsFrequencyPenaltyReasoningEffort(enum.StrEnum):
    NONE = "none"
    MINIMAL = "minimal"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        minimal: typing.Callable[[], T_Result],
        low: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ModelParamsFrequencyPenaltyReasoningEffort.NONE:
            return none()
        if self is ModelParamsFrequencyPenaltyReasoningEffort.MINIMAL:
            return minimal()
        if self is ModelParamsFrequencyPenaltyReasoningEffort.LOW:
            return low()
        if self is ModelParamsFrequencyPenaltyReasoningEffort.MEDIUM:
            return medium()
        if self is ModelParamsFrequencyPenaltyReasoningEffort.HIGH:
            return high()
