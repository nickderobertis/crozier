

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelOptionsWhatsappChannel(enum.StrEnum):
    """
    The channel to send to. You must provide `whatsapp` in this field
    """

    WHATSAPP = "whatsapp"

    def visit(self, whatsapp: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChannelOptionsWhatsappChannel.WHATSAPP:
            return whatsapp()
