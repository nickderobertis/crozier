

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunStepObjectType(enum.StrEnum):
    """
    The type of run step, which can be either `message_creation` or `tool_calls`.
    """

    MESSAGE_CREATION = "message_creation"
    TOOL_CALLS = "tool_calls"

    def visit(
        self, message_creation: typing.Callable[[], T_Result], tool_calls: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is RunStepObjectType.MESSAGE_CREATION:
            return message_creation()
        if self is RunStepObjectType.TOOL_CALLS:
            return tool_calls()
