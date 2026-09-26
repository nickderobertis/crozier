

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReplyMessageType(enum.StrEnum):
    """
    The type of message to send. You must provide `custom` in this field.
    """

    REPLY = "reply"

    def visit(self, reply: typing.Callable[[], T_Result]) -> T_Result:
        if self is ReplyMessageType.REPLY:
            return reply()
