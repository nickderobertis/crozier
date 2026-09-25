

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UnsupportedMessageType(enum.StrEnum):
    """
    The type of message to send. Will be `unsupported` if the type of message received from user is not supported by the channel.
    """

    UNSUPPORTED = "unsupported"

    def visit(self, unsupported: typing.Callable[[], T_Result]) -> T_Result:
        if self is UnsupportedMessageType.UNSUPPORTED:
            return unsupported()
