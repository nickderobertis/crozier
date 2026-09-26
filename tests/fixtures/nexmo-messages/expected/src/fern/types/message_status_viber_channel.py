

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageStatusViberChannel(enum.StrEnum):
    """
    The channel sending to.
    """

    VIBER_SERVICE = "viber_service"

    def visit(self, viber_service: typing.Callable[[], T_Result]) -> T_Result:
        if self is MessageStatusViberChannel.VIBER_SERVICE:
            return viber_service()
