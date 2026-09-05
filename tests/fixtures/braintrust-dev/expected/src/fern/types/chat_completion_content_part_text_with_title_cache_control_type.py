

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatCompletionContentPartTextWithTitleCacheControlType(enum.StrEnum):
    EPHEMERAL = "ephemeral"

    def visit(self, ephemeral: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChatCompletionContentPartTextWithTitleCacheControlType.EPHEMERAL:
            return ephemeral()
