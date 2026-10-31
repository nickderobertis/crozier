

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatMessageRole(enum.StrEnum):
    """
    Author of the message.
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
        if self is ChatMessageRole.SYSTEM:
            return system()
        if self is ChatMessageRole.USER:
            return user()
        if self is ChatMessageRole.ASSISTANT:
            return assistant()
        if self is ChatMessageRole.TOOL:
            return tool()
