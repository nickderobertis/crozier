

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageStatusSmsChannel(enum.StrEnum):
    """
    The channel sending to.
    """

    SMS = "sms"

    def visit(self, sms: typing.Callable[[], T_Result]) -> T_Result:
        if self is MessageStatusSmsChannel.SMS:
            return sms()
