

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RefundStatus(enum.StrEnum):
    """
    Indicates a refund's current status.
    """

    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    FAILED = "FAILED"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RefundStatus.PENDING:
            return pending()
        if self is RefundStatus.APPROVED:
            return approved()
        if self is RefundStatus.REJECTED:
            return rejected()
        if self is RefundStatus.FAILED:
            return failed()
