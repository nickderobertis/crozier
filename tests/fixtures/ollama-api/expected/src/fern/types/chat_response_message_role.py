

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatResponseMessageRole(enum.StrEnum):
    """
    Always `assistant` for model responses
    """

    ASSISTANT = "assistant"

    def visit(self, assistant: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChatResponseMessageRole.ASSISTANT:
            return assistant()
