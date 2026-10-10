

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OpenAiMessageRole(enum.StrEnum):
    ASSISTANT = "assistant"
    SYSTEM = "system"
    USER = "user"

    def visit(
        self,
        assistant: typing.Callable[[], T_Result],
        system: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OpenAiMessageRole.ASSISTANT:
            return assistant()
        if self is OpenAiMessageRole.SYSTEM:
            return system()
        if self is OpenAiMessageRole.USER:
            return user()
