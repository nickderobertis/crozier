

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelOptionsMessengerChannel(enum.StrEnum):
    """
    The channel to send to. You must provide `messenger` in this field
    """

    MESSENGER = "messenger"

    def visit(self, messenger: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChannelOptionsMessengerChannel.MESSENGER:
            return messenger()
