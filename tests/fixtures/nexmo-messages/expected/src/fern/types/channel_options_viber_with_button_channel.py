

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelOptionsViberWithButtonChannel(enum.StrEnum):
    """
    The channel to send to. You must provide `viber_service` in this field
    """

    VIBER_SERVICE = "viber_service"

    def visit(self, viber_service: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChannelOptionsViberWithButtonChannel.VIBER_SERVICE:
            return viber_service()
