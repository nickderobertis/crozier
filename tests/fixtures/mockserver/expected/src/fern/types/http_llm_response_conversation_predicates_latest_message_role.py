

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HttpLlmResponseConversationPredicatesLatestMessageRole(enum.StrEnum):
    USER = "USER"
    ASSISTANT = "ASSISTANT"
    TOOL = "TOOL"
    SYSTEM = "SYSTEM"

    def visit(
        self,
        user: typing.Callable[[], T_Result],
        assistant: typing.Callable[[], T_Result],
        tool: typing.Callable[[], T_Result],
        system: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HttpLlmResponseConversationPredicatesLatestMessageRole.USER:
            return user()
        if self is HttpLlmResponseConversationPredicatesLatestMessageRole.ASSISTANT:
            return assistant()
        if self is HttpLlmResponseConversationPredicatesLatestMessageRole.TOOL:
            return tool()
        if self is HttpLlmResponseConversationPredicatesLatestMessageRole.SYSTEM:
            return system()
