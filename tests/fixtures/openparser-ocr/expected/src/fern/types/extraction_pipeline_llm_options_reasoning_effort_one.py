

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExtractionPipelineLlmOptionsReasoningEffortOne(enum.StrEnum):
    NONE = "none"
    MINIMAL = "minimal"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    XHIGH = "xhigh"
    MAX = "max"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        minimal: typing.Callable[[], T_Result],
        low: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
        xhigh: typing.Callable[[], T_Result],
        max: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExtractionPipelineLlmOptionsReasoningEffortOne.NONE:
            return none()
        if self is ExtractionPipelineLlmOptionsReasoningEffortOne.MINIMAL:
            return minimal()
        if self is ExtractionPipelineLlmOptionsReasoningEffortOne.LOW:
            return low()
        if self is ExtractionPipelineLlmOptionsReasoningEffortOne.MEDIUM:
            return medium()
        if self is ExtractionPipelineLlmOptionsReasoningEffortOne.HIGH:
            return high()
        if self is ExtractionPipelineLlmOptionsReasoningEffortOne.XHIGH:
            return xhigh()
        if self is ExtractionPipelineLlmOptionsReasoningEffortOne.MAX:
            return max()
