

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UiMessageResponseRole(enum.StrEnum):
    USER = "user"
    ASSISTANT = "assistant"

    def visit(self, user: typing.Callable[[], T_Result], assistant: typing.Callable[[], T_Result]) -> T_Result:
        if self is UiMessageResponseRole.USER:
            return user()
        if self is UiMessageResponseRole.ASSISTANT:
            return assistant()
