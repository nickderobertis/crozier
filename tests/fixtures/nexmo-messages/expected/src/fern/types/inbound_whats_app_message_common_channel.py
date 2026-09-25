

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InboundWhatsAppMessageCommonChannel(enum.StrEnum):
    """
    The channel that the message came in on
    """

    WHATSAPP = "whatsapp"

    def visit(self, whatsapp: typing.Callable[[], T_Result]) -> T_Result:
        if self is InboundWhatsAppMessageCommonChannel.WHATSAPP:
            return whatsapp()
