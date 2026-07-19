

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelReasoningEffort(enum.StrEnum):
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
        if self is ModelReasoningEffort.NONE:
            return none()
        if self is ModelReasoningEffort.MINIMAL:
            return minimal()
        if self is ModelReasoningEffort.LOW:
            return low()
        if self is ModelReasoningEffort.MEDIUM:
            return medium()
        if self is ModelReasoningEffort.HIGH:
            return high()
        if self is ModelReasoningEffort.XHIGH:
            return xhigh()
