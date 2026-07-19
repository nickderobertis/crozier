

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatGptoAuthReasoningReasoningEffort(enum.StrEnum):
    """
    The reasoning effort level for GPT-5.x and o-series models.
    """

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
        if self is ChatGptoAuthReasoningReasoningEffort.NONE:
            return none()
        if self is ChatGptoAuthReasoningReasoningEffort.LOW:
            return low()
        if self is ChatGptoAuthReasoningReasoningEffort.MEDIUM:
            return medium()
        if self is ChatGptoAuthReasoningReasoningEffort.HIGH:
            return high()
        if self is ChatGptoAuthReasoningReasoningEffort.XHIGH:
            return xhigh()
