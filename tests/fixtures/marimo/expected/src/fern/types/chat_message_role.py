

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatMessageRole(enum.StrEnum):
    ASSISTANT = "assistant"
    SYSTEM = "system"
    USER = "user"

    def visit(
        self,
        assistant: typing.Callable[[], T_Result],
        system: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChatMessageRole.ASSISTANT:
            return assistant()
        if self is ChatMessageRole.SYSTEM:
            return system()
        if self is ChatMessageRole.USER:
            return user()
