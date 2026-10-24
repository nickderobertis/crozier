

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageSummaryObject(enum.StrEnum):
    """
    Object type identifier
    """

    MESSAGE = "message"

    def visit(self, message: typing.Callable[[], T_Result]) -> T_Result:
        if self is MessageSummaryObject.MESSAGE:
            return message()
