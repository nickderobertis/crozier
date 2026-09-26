

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InboundMessageSmsChannel(enum.StrEnum):
    """
    The channel the message came in on
    """

    SMS = "sms"

    def visit(self, sms: typing.Callable[[], T_Result]) -> T_Result:
        if self is InboundMessageSmsChannel.SMS:
            return sms()
