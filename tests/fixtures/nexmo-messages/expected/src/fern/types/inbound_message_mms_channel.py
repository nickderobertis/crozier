

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InboundMessageMmsChannel(enum.StrEnum):
    """
    The channel the message came in on
    """

    MMS = "mms"

    def visit(self, mms: typing.Callable[[], T_Result]) -> T_Result:
        if self is InboundMessageMmsChannel.MMS:
            return mms()
