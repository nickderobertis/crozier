

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ChatCompletionRequestServiceTier(enum.StrEnum):
    AUTO = "auto"
    DEFAULT = "default"
    FLEX = "flex"
    SCALE = "scale"
    PRIORITY = "priority"

    def visit(
        self,
        auto: typing.Callable[[], T_Result],
        default: typing.Callable[[], T_Result],
        flex: typing.Callable[[], T_Result],
        scale: typing.Callable[[], T_Result],
        priority: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChatCompletionRequestServiceTier.AUTO:
            return auto()
        if self is ChatCompletionRequestServiceTier.DEFAULT:
            return default()
        if self is ChatCompletionRequestServiceTier.FLEX:
            return flex()
        if self is ChatCompletionRequestServiceTier.SCALE:
            return scale()
        if self is ChatCompletionRequestServiceTier.PRIORITY:
            return priority()
