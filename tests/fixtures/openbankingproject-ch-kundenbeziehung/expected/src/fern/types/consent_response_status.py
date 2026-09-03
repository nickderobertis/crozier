

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConsentResponseStatus(enum.StrEnum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    EXPIRED = "expired"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConsentResponseStatus.PENDING:
            return pending()
        if self is ConsentResponseStatus.APPROVED:
            return approved()
        if self is ConsentResponseStatus.REJECTED:
            return rejected()
        if self is ConsentResponseStatus.EXPIRED:
            return expired()
