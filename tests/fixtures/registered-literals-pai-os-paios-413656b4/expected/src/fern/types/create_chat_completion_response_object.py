

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateChatCompletionResponseObject(enum.StrEnum):
    """
    The object type, which is always `chat.completion`.
    """

    CHAT_COMPLETION = "chat.completion"

    def visit(self, chat_completion: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateChatCompletionResponseObject.CHAT_COMPLETION:
            return chat_completion()
