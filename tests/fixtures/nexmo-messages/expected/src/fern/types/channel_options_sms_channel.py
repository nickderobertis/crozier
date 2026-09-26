

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelOptionsSmsChannel(enum.StrEnum):
    """
    The channel to send to. You must provide `sms` in this field
    """

    SMS = "sms"

    def visit(self, sms: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChannelOptionsSmsChannel.SMS:
            return sms()
