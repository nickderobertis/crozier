

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatCompletionResponseMessageRole(enum.StrEnum):
    """
    The role of the author of this message.
    """

    ASSISTANT = "assistant"

    def visit(self, assistant: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChatCompletionResponseMessageRole.ASSISTANT:
            return assistant()
