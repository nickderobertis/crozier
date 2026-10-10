

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReasoningEffort(enum.StrEnum):
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
        if self is ReasoningEffort.NONE:
            return none()
        if self is ReasoningEffort.MINIMAL:
            return minimal()
        if self is ReasoningEffort.LOW:
            return low()
        if self is ReasoningEffort.MEDIUM:
            return medium()
        if self is ReasoningEffort.HIGH:
            return high()
        if self is ReasoningEffort.XHIGH:
            return xhigh()
        if self is ReasoningEffort.MAX:
            return max()
