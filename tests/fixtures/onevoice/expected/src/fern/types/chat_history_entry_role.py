

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatHistoryEntryRole(enum.StrEnum):
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
        if self is ChatHistoryEntryRole.SYSTEM:
            return system()
        if self is ChatHistoryEntryRole.USER:
            return user()
        if self is ChatHistoryEntryRole.ASSISTANT:
            return assistant()
        if self is ChatHistoryEntryRole.TOOL:
            return tool()
