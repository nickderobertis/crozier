

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConsentStatusStatus(enum.StrEnum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    EXPIRED = "expired"
    REVOKED = "revoked"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
        revoked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConsentStatusStatus.PENDING:
            return pending()
        if self is ConsentStatusStatus.APPROVED:
            return approved()
        if self is ConsentStatusStatus.REJECTED:
            return rejected()
        if self is ConsentStatusStatus.EXPIRED:
            return expired()
        if self is ConsentStatusStatus.REVOKED:
            return revoked()
