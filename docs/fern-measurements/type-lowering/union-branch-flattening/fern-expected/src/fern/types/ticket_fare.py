

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TicketFare(enum.StrEnum):
    ADULT = "adult"

    def visit(self, adult: typing.Callable[[], T_Result]) -> T_Result:
        if self is TicketFare.ADULT:
            return adult()
