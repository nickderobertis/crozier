

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PdfActionTreeWarningsItem(enum.StrEnum):
    CYCLE_DROPPED = "cycle-dropped"
    MALFORMED_NEXT = "malformed-next"
    INCOMPLETE = "incomplete"
    PAYLOAD_DROPPED = "payload-dropped"

    def visit(
        self,
        cycle_dropped: typing.Callable[[], T_Result],
        malformed_next: typing.Callable[[], T_Result],
        incomplete: typing.Callable[[], T_Result],
        payload_dropped: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PdfActionTreeWarningsItem.CYCLE_DROPPED:
            return cycle_dropped()
        if self is PdfActionTreeWarningsItem.MALFORMED_NEXT:
            return malformed_next()
        if self is PdfActionTreeWarningsItem.INCOMPLETE:
            return incomplete()
        if self is PdfActionTreeWarningsItem.PAYLOAD_DROPPED:
            return payload_dropped()
