

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExtractBatchItemLlmOptionsReasoningEffortOne(enum.StrEnum):
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
        if self is ExtractBatchItemLlmOptionsReasoningEffortOne.NONE:
            return none()
        if self is ExtractBatchItemLlmOptionsReasoningEffortOne.MINIMAL:
            return minimal()
        if self is ExtractBatchItemLlmOptionsReasoningEffortOne.LOW:
            return low()
        if self is ExtractBatchItemLlmOptionsReasoningEffortOne.MEDIUM:
            return medium()
        if self is ExtractBatchItemLlmOptionsReasoningEffortOne.HIGH:
            return high()
        if self is ExtractBatchItemLlmOptionsReasoningEffortOne.XHIGH:
            return xhigh()
        if self is ExtractBatchItemLlmOptionsReasoningEffortOne.MAX:
            return max()
