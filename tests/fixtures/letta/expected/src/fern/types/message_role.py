

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageRole(enum.StrEnum):
    ASSISTANT = "assistant"
    USER = "user"
    TOOL = "tool"
    FUNCTION = "function"
    SYSTEM = "system"
    APPROVAL = "approval"

    def visit(
        self,
        assistant: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
        tool: typing.Callable[[], T_Result],
        function: typing.Callable[[], T_Result],
        system: typing.Callable[[], T_Result],
        approval: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MessageRole.ASSISTANT:
            return assistant()
        if self is MessageRole.USER:
            return user()
        if self is MessageRole.TOOL:
            return tool()
        if self is MessageRole.FUNCTION:
            return function()
        if self is MessageRole.SYSTEM:
            return system()
        if self is MessageRole.APPROVAL:
            return approval()
