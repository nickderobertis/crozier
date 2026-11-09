

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CommonTicketPriority(enum.StrEnum):
    URGENT = "urgent"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    LOWEST = "lowest"

    def visit(
        self,
        urgent: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        low: typing.Callable[[], T_Result],
        lowest: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CommonTicketPriority.URGENT:
            return urgent()
        if self is CommonTicketPriority.HIGH:
            return high()
        if self is CommonTicketPriority.MEDIUM:
            return medium()
        if self is CommonTicketPriority.LOW:
            return low()
        if self is CommonTicketPriority.LOWEST:
            return lowest()
