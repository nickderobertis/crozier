

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageStatusMessengerChannel(enum.StrEnum):
    """
    The channel sending to.
    """

    MESSENGER = "messenger"

    def visit(self, messenger: typing.Callable[[], T_Result]) -> T_Result:
        if self is MessageStatusMessengerChannel.MESSENGER:
            return messenger()
