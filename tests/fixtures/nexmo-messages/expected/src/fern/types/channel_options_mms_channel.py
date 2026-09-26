

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelOptionsMmsChannel(enum.StrEnum):
    """
    The channel to send to. You must provide `mms` in this field
    """

    MMS = "mms"

    def visit(self, mms: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChannelOptionsMmsChannel.MMS:
            return mms()
