

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ConversationThresholdPutResponseThreshold(enum.StrEnum):
    NONE = "none"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        low: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConversationThresholdPutResponseThreshold.NONE:
            return none()
        if self is ConversationThresholdPutResponseThreshold.LOW:
            return low()
        if self is ConversationThresholdPutResponseThreshold.MEDIUM:
            return medium()
        if self is ConversationThresholdPutResponseThreshold.HIGH:
            return high()
