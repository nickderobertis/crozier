

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatCompletionObject(enum.StrEnum):
    CHAT_COMPLETION = "chat.completion"

    def visit(self, chat_completion: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChatCompletionObject.CHAT_COMPLETION:
            return chat_completion()
