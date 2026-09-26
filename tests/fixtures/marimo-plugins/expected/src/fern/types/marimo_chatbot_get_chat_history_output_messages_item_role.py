

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoChatbotGetChatHistoryOutputMessagesItemRole(enum.StrEnum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"

    def visit(
        self,
        system: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
        assistant: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MarimoChatbotGetChatHistoryOutputMessagesItemRole.SYSTEM:
            return system()
        if self is MarimoChatbotGetChatHistoryOutputMessagesItemRole.USER:
            return user()
        if self is MarimoChatbotGetChatHistoryOutputMessagesItemRole.ASSISTANT:
            return assistant()
