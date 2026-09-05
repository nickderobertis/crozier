

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatCompletionContentPartTextCacheControlType(enum.StrEnum):
    EPHEMERAL = "ephemeral"

    def visit(self, ephemeral: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChatCompletionContentPartTextCacheControlType.EPHEMERAL:
            return ephemeral()
