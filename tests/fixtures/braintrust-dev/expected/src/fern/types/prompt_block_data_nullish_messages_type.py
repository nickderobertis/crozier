

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PromptBlockDataNullishMessagesType(enum.StrEnum):
    CHAT = "chat"

    def visit(self, chat: typing.Callable[[], T_Result]) -> T_Result:
        if self is PromptBlockDataNullishMessagesType.CHAT:
            return chat()
