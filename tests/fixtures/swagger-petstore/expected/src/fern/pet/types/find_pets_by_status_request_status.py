

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class FindPetsByStatusRequestStatus(enum.StrEnum):
    AVAILABLE = "available"
    PENDING = "pending"
    SOLD = "sold"

    def visit(
        self,
        available: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        sold: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FindPetsByStatusRequestStatus.AVAILABLE:
            return available()
        if self is FindPetsByStatusRequestStatus.PENDING:
            return pending()
        if self is FindPetsByStatusRequestStatus.SOLD:
            return sold()
