

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatCompletionStreamResponseDeltaRole(enum.StrEnum):
    """
    The role of the author of this message.
    """

    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"

    def visit(
        self,
        system: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
        assistant: typing.Callable[[], T_Result],
        tool: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChatCompletionStreamResponseDeltaRole.SYSTEM:
            return system()
        if self is ChatCompletionStreamResponseDeltaRole.USER:
            return user()
        if self is ChatCompletionStreamResponseDeltaRole.ASSISTANT:
            return assistant()
        if self is ChatCompletionStreamResponseDeltaRole.TOOL:
            return tool()
