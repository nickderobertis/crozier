

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TemplatesCreateAgentsFromTemplateNoProjectRequestInitialMessageSequenceItemRole(enum.StrEnum):
    USER = "user"
    SYSTEM = "system"
    ASSISTANT = "assistant"

    def visit(
        self,
        user: typing.Callable[[], T_Result],
        system: typing.Callable[[], T_Result],
        assistant: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TemplatesCreateAgentsFromTemplateNoProjectRequestInitialMessageSequenceItemRole.USER:
            return user()
        if self is TemplatesCreateAgentsFromTemplateNoProjectRequestInitialMessageSequenceItemRole.SYSTEM:
            return system()
        if self is TemplatesCreateAgentsFromTemplateNoProjectRequestInitialMessageSequenceItemRole.ASSISTANT:
            return assistant()
