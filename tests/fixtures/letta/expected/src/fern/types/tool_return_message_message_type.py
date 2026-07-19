

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ToolReturnMessageMessageType(enum.StrEnum):
    """
    The type of the message.
    """

    TOOL_RETURN_MESSAGE = "tool_return_message"

    def visit(self, tool_return_message: typing.Callable[[], T_Result]) -> T_Result:
        if self is ToolReturnMessageMessageType.TOOL_RETURN_MESSAGE:
            return tool_return_message()
