

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageRole(enum.StrEnum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"

    def visit(
        self,
        user: typing.Callable[[], T_Result],
        assistant: typing.Callable[[], T_Result],
        system: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MessageRole.USER:
            return user()
        if self is MessageRole.ASSISTANT:
            return assistant()
        if self is MessageRole.SYSTEM:
            return system()
