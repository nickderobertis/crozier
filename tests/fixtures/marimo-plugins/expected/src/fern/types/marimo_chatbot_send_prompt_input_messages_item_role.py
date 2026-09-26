

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoChatbotSendPromptInputMessagesItemRole(enum.StrEnum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"

    def visit(
        self,
        system: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
        assistant: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MarimoChatbotSendPromptInputMessagesItemRole.SYSTEM:
            return system()
        if self is MarimoChatbotSendPromptInputMessagesItemRole.USER:
            return user()
        if self is MarimoChatbotSendPromptInputMessagesItemRole.ASSISTANT:
            return assistant()
