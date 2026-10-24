

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageSummaryDirection(enum.StrEnum):
    """
    Message direction
    """

    INBOUND = "inbound"
    OUTBOUND = "outbound"

    def visit(self, inbound: typing.Callable[[], T_Result], outbound: typing.Callable[[], T_Result]) -> T_Result:
        if self is MessageSummaryDirection.INBOUND:
            return inbound()
        if self is MessageSummaryDirection.OUTBOUND:
            return outbound()
