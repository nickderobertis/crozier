

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatCompletionMessageRole(enum.StrEnum):
    ASSISTANT = "assistant"

    def visit(self, assistant: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChatCompletionMessageRole.ASSISTANT:
            return assistant()
