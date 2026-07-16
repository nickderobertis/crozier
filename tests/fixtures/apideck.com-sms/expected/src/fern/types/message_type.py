

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageType(enum.StrEnum):
    """
    Set to sms for SMS messages and mms for MMS messages.
    """

    SMS = "sms"
    MMS = "mms"

    def visit(self, sms: typing.Callable[[], T_Result], mms: typing.Callable[[], T_Result]) -> T_Result:
        if self is MessageType.SMS:
            return sms()
        if self is MessageType.MMS:
            return mms()
