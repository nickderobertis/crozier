

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InboundViberMessageCommonChannel(enum.StrEnum):
    """
    The channel that the message came in on
    """

    VIBER_SERVICE = "viber_service"

    def visit(self, viber_service: typing.Callable[[], T_Result]) -> T_Result:
        if self is InboundViberMessageCommonChannel.VIBER_SERVICE:
            return viber_service()
