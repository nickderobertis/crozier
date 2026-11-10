

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatCompletionRole(enum.StrEnum):
    """
    The role of the author of a message
    """

    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"
    FUNCTION = "function"

    def visit(
        self,
        system: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
        assistant: typing.Callable[[], T_Result],
        tool: typing.Callable[[], T_Result],
        function: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChatCompletionRole.SYSTEM:
            return system()
        if self is ChatCompletionRole.USER:
            return user()
        if self is ChatCompletionRole.ASSISTANT:
            return assistant()
        if self is ChatCompletionRole.TOOL:
            return tool()
        if self is ChatCompletionRole.FUNCTION:
            return function()
