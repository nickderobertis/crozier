

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PetStatus(enum.StrEnum):
    """
    pet status in the store
    """

    AVAILABLE = "available"
    PENDING = "pending"
    SOLD = "sold"

    def visit(
        self,
        available: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        sold: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PetStatus.AVAILABLE:
            return available()
        if self is PetStatus.PENDING:
            return pending()
        if self is PetStatus.SOLD:
            return sold()
