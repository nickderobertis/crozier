

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TicketsSortBy(enum.StrEnum):
    """
    The field on which to sort the Tickets
    """

    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"

    def visit(self, created_at: typing.Callable[[], T_Result], updated_at: typing.Callable[[], T_Result]) -> T_Result:
        if self is TicketsSortBy.CREATED_AT:
            return created_at()
        if self is TicketsSortBy.UPDATED_AT:
            return updated_at()
