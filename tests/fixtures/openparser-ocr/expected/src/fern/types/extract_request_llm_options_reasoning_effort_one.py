

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExtractRequestLlmOptionsReasoningEffortOne(enum.StrEnum):
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
        if self is ExtractRequestLlmOptionsReasoningEffortOne.NONE:
            return none()
        if self is ExtractRequestLlmOptionsReasoningEffortOne.MINIMAL:
            return minimal()
        if self is ExtractRequestLlmOptionsReasoningEffortOne.LOW:
            return low()
        if self is ExtractRequestLlmOptionsReasoningEffortOne.MEDIUM:
            return medium()
        if self is ExtractRequestLlmOptionsReasoningEffortOne.HIGH:
            return high()
        if self is ExtractRequestLlmOptionsReasoningEffortOne.XHIGH:
            return xhigh()
        if self is ExtractRequestLlmOptionsReasoningEffortOne.MAX:
            return max()
