

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OpenAiReasoningReasoningEffort(enum.StrEnum):
    """
    The reasoning effort to use when generating text reasoning models
    """

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
        if self is OpenAiReasoningReasoningEffort.NONE:
            return none()
        if self is OpenAiReasoningReasoningEffort.MINIMAL:
            return minimal()
        if self is OpenAiReasoningReasoningEffort.LOW:
            return low()
        if self is OpenAiReasoningReasoningEffort.MEDIUM:
            return medium()
        if self is OpenAiReasoningReasoningEffort.HIGH:
            return high()
        if self is OpenAiReasoningReasoningEffort.XHIGH:
            return xhigh()
