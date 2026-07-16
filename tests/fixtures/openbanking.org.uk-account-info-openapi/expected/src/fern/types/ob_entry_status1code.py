

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObEntryStatus1Code(enum.StrEnum):
    """
    Status of a transaction entry on the books of the account servicer.
    """

    BOOKED = "Booked"
    PENDING = "Pending"

    def visit(self, booked: typing.Callable[[], T_Result], pending: typing.Callable[[], T_Result]) -> T_Result:
        if self is ObEntryStatus1Code.BOOKED:
            return booked()
        if self is ObEntryStatus1Code.PENDING:
            return pending()
