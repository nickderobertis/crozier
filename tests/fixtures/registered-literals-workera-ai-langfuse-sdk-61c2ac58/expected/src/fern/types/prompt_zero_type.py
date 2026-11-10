

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PromptZeroType(enum.StrEnum):
    CHAT = "chat"

    def visit(self, chat: typing.Callable[[], T_Result]) -> T_Result:
        if self is PromptZeroType.CHAT:
            return chat()
