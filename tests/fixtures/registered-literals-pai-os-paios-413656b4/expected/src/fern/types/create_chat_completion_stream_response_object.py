

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateChatCompletionStreamResponseObject(enum.StrEnum):
    """
    The object type, which is always `chat.completion.chunk`.
    """

    CHAT_COMPLETION_CHUNK = "chat.completion.chunk"

    def visit(self, chat_completion_chunk: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateChatCompletionStreamResponseObject.CHAT_COMPLETION_CHUNK:
            return chat_completion_chunk()
