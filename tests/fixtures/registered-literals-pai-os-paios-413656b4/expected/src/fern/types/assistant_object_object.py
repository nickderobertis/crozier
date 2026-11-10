

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssistantObjectObject(enum.StrEnum):
    """
    The object type, which is always `assistant`.
    """

    ASSISTANT = "assistant"

    def visit(self, assistant: typing.Callable[[], T_Result]) -> T_Result:
        if self is AssistantObjectObject.ASSISTANT:
            return assistant()
