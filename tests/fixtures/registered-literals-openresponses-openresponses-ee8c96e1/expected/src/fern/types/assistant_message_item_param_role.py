

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssistantMessageItemParamRole(enum.StrEnum):
    """
    The role of the message author. Always `assistant`.
    """

    ASSISTANT = "assistant"

    def visit(self, assistant: typing.Callable[[], T_Result]) -> T_Result:
        if self is AssistantMessageItemParamRole.ASSISTANT:
            return assistant()
