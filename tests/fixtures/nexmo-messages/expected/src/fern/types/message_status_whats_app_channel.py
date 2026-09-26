

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageStatusWhatsAppChannel(enum.StrEnum):
    """
    The channel sending to.
    """

    WHATSAPP = "whatsapp"

    def visit(self, whatsapp: typing.Callable[[], T_Result]) -> T_Result:
        if self is MessageStatusWhatsAppChannel.WHATSAPP:
            return whatsapp()
