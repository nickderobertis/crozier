

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BankTransferEventType(enum.StrEnum):
    """
    The type of event that this bank transfer represents.

    `pending`: A new transfer was created; it is in the pending state.

    `cancelled`: The transfer was cancelled by the client.

    `failed`: The transfer failed, no funds were moved.

    `posted`: The transfer has been successfully submitted to the payment network.

    `reversed`: A posted transfer was reversed.
    """

    PENDING = "pending"
    CANCELLED = "cancelled"
    FAILED = "failed"
    POSTED = "posted"
    REVERSED = "reversed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        posted: typing.Callable[[], T_Result],
        reversed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BankTransferEventType.PENDING:
            return pending()
        if self is BankTransferEventType.CANCELLED:
            return cancelled()
        if self is BankTransferEventType.FAILED:
            return failed()
        if self is BankTransferEventType.POSTED:
            return posted()
        if self is BankTransferEventType.REVERSED:
            return reversed()
