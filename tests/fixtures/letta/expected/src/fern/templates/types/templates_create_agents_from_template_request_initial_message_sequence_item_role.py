

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TemplatesCreateAgentsFromTemplateRequestInitialMessageSequenceItemRole(enum.StrEnum):
    USER = "user"
    SYSTEM = "system"
    ASSISTANT = "assistant"

    def visit(
        self,
        user: typing.Callable[[], T_Result],
        system: typing.Callable[[], T_Result],
        assistant: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TemplatesCreateAgentsFromTemplateRequestInitialMessageSequenceItemRole.USER:
            return user()
        if self is TemplatesCreateAgentsFromTemplateRequestInitialMessageSequenceItemRole.SYSTEM:
            return system()
        if self is TemplatesCreateAgentsFromTemplateRequestInitialMessageSequenceItemRole.ASSISTANT:
            return assistant()
