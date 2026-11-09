

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BankTransferStatus(enum.StrEnum):
    """
    The status of the transfer.
    """

    PENDING = "pending"
    POSTED = "posted"
    CANCELLED = "cancelled"
    FAILED = "failed"
    REVERSED = "reversed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        posted: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        reversed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BankTransferStatus.PENDING:
            return pending()
        if self is BankTransferStatus.POSTED:
            return posted()
        if self is BankTransferStatus.CANCELLED:
            return cancelled()
        if self is BankTransferStatus.FAILED:
            return failed()
        if self is BankTransferStatus.REVERSED:
            return reversed()
