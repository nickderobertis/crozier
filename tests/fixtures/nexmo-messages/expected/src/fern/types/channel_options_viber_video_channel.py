

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelOptionsViberVideoChannel(enum.StrEnum):
    """
    The channel to send to. You must provide `viber_service` in this field
    """

    VIBER_SERVICE = "viber_service"

    def visit(self, viber_service: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChannelOptionsViberVideoChannel.VIBER_SERVICE:
            return viber_service()
