

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PendingApprovalStatus(enum.StrEnum):
    """
    Unavailable means the batch was physically removed; it does not assert whether the tool executed.
    """

    PENDING = "pending"
    RESOLVING = "resolving"
    EXPIRED = "expired"
    UNAVAILABLE = "unavailable"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        resolving: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
        unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PendingApprovalStatus.PENDING:
            return pending()
        if self is PendingApprovalStatus.RESOLVING:
            return resolving()
        if self is PendingApprovalStatus.EXPIRED:
            return expired()
        if self is PendingApprovalStatus.UNAVAILABLE:
            return unavailable()
