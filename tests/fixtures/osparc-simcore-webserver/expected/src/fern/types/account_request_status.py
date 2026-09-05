

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AccountRequestStatus(enum.StrEnum):
    """
    Status of the request for an account
    """

    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AccountRequestStatus.PENDING:
            return pending()
        if self is AccountRequestStatus.APPROVED:
            return approved()
        if self is AccountRequestStatus.REJECTED:
            return rejected()
