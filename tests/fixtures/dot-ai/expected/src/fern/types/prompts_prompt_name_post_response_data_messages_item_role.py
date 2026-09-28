

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PromptsPromptNamePostResponseDataMessagesItemRole(enum.StrEnum):
    """
    Message role
    """

    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"

    def visit(
        self,
        user: typing.Callable[[], T_Result],
        assistant: typing.Callable[[], T_Result],
        system: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PromptsPromptNamePostResponseDataMessagesItemRole.USER:
            return user()
        if self is PromptsPromptNamePostResponseDataMessagesItemRole.ASSISTANT:
            return assistant()
        if self is PromptsPromptNamePostResponseDataMessagesItemRole.SYSTEM:
            return system()
