

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageStatusMmsChannel(enum.StrEnum):
    """
    The channel sending to.
    """

    MMS = "mms"

    def visit(self, mms: typing.Callable[[], T_Result]) -> T_Result:
        if self is MessageStatusMmsChannel.MMS:
            return mms()
