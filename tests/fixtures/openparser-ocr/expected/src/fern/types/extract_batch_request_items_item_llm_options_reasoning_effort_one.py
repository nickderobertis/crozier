

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExtractBatchRequestItemsItemLlmOptionsReasoningEffortOne(enum.StrEnum):
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
        if self is ExtractBatchRequestItemsItemLlmOptionsReasoningEffortOne.NONE:
            return none()
        if self is ExtractBatchRequestItemsItemLlmOptionsReasoningEffortOne.MINIMAL:
            return minimal()
        if self is ExtractBatchRequestItemsItemLlmOptionsReasoningEffortOne.LOW:
            return low()
        if self is ExtractBatchRequestItemsItemLlmOptionsReasoningEffortOne.MEDIUM:
            return medium()
        if self is ExtractBatchRequestItemsItemLlmOptionsReasoningEffortOne.HIGH:
            return high()
        if self is ExtractBatchRequestItemsItemLlmOptionsReasoningEffortOne.XHIGH:
            return xhigh()
        if self is ExtractBatchRequestItemsItemLlmOptionsReasoningEffortOne.MAX:
            return max()
