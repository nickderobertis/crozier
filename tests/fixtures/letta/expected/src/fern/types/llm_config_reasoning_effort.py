

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LlmConfigReasoningEffort(enum.StrEnum):
    NONE = "none"
    MINIMAL = "minimal"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    XHIGH = "xhigh"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        minimal: typing.Callable[[], T_Result],
        low: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
        xhigh: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LlmConfigReasoningEffort.NONE:
            return none()
        if self is LlmConfigReasoningEffort.MINIMAL:
            return minimal()
        if self is LlmConfigReasoningEffort.LOW:
            return low()
        if self is LlmConfigReasoningEffort.MEDIUM:
            return medium()
        if self is LlmConfigReasoningEffort.HIGH:
            return high()
        if self is LlmConfigReasoningEffort.XHIGH:
            return xhigh()
