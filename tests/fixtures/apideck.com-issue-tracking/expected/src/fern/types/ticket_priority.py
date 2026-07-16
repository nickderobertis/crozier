

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TicketPriority(enum.StrEnum):
    """
    Priority of the ticket
    """

    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    URGENT = "urgent"

    def visit(
        self,
        low: typing.Callable[[], T_Result],
        normal: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
        urgent: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TicketPriority.LOW:
            return low()
        if self is TicketPriority.NORMAL:
            return normal()
        if self is TicketPriority.HIGH:
            return high()
        if self is TicketPriority.URGENT:
            return urgent()
