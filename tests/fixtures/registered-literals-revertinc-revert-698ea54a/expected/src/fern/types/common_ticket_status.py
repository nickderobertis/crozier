

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CommonTicketStatus(enum.StrEnum):
    OPEN = "open"
    CLOSE = "close"
    IN_PROGRESS = "in_progress"

    def visit(
        self,
        open: typing.Callable[[], T_Result],
        close: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CommonTicketStatus.OPEN:
            return open()
        if self is CommonTicketStatus.CLOSE:
            return close()
        if self is CommonTicketStatus.IN_PROGRESS:
            return in_progress()
