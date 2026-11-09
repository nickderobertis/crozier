

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CallNotificationParametersDirection(enum.StrEnum):
    """
    Call's direction
    """

    INBOUND = "inbound"
    OUTBOUND = "outbound"

    def visit(self, inbound: typing.Callable[[], T_Result], outbound: typing.Callable[[], T_Result]) -> T_Result:
        if self is CallNotificationParametersDirection.INBOUND:
            return inbound()
        if self is CallNotificationParametersDirection.OUTBOUND:
            return outbound()
