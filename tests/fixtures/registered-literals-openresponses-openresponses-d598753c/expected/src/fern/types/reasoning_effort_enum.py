

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReasoningEffortEnum(enum.StrEnum):
    NONE = "none"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    XHIGH = "xhigh"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        low: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
        xhigh: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReasoningEffortEnum.NONE:
            return none()
        if self is ReasoningEffortEnum.LOW:
            return low()
        if self is ReasoningEffortEnum.MEDIUM:
            return medium()
        if self is ReasoningEffortEnum.HIGH:
            return high()
        if self is ReasoningEffortEnum.XHIGH:
            return xhigh()
