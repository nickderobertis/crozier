

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatCompletionServiceTier(enum.StrEnum):
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
        if self is ChatCompletionServiceTier.AUTO:
            return auto()
        if self is ChatCompletionServiceTier.DEFAULT:
            return default()
        if self is ChatCompletionServiceTier.FLEX:
            return flex()
        if self is ChatCompletionServiceTier.SCALE:
            return scale()
        if self is ChatCompletionServiceTier.PRIORITY:
            return priority()
