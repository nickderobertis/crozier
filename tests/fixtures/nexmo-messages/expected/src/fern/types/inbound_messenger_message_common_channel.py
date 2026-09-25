

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InboundMessengerMessageCommonChannel(enum.StrEnum):
    """
    The channel that the message came in on
    """

    MESSENGER = "messenger"

    def visit(self, messenger: typing.Callable[[], T_Result]) -> T_Result:
        if self is InboundMessengerMessageCommonChannel.MESSENGER:
            return messenger()
