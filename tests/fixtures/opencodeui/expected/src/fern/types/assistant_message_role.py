

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssistantMessageRole(enum.StrEnum):
    ASSISTANT = "assistant"

    def visit(self, assistant: typing.Callable[[], T_Result]) -> T_Result:
        if self is AssistantMessageRole.ASSISTANT:
            return assistant()
