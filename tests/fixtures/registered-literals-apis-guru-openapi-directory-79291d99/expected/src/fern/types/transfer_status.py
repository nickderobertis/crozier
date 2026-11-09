

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransferStatus(enum.StrEnum):
    """
    The status of the transfer.

    `pending`: A new transfer was created; it is in the pending state.
    `posted`: The transfer has been successfully submitted to the payment network.
    `settled`: Credits are available to be withdrawn or debits have been deducted from the Plaid linked account.
    `cancelled`: The transfer was cancelled by the client.
    `failed`: The transfer failed, no funds were moved.
    `returned`: A posted transfer was returned.
    """

    PENDING = "pending"
    POSTED = "posted"
    SETTLED = "settled"
    CANCELLED = "cancelled"
    FAILED = "failed"
    RETURNED = "returned"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        posted: typing.Callable[[], T_Result],
        settled: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        returned: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransferStatus.PENDING:
            return pending()
        if self is TransferStatus.POSTED:
            return posted()
        if self is TransferStatus.SETTLED:
            return settled()
        if self is TransferStatus.CANCELLED:
            return cancelled()
        if self is TransferStatus.FAILED:
            return failed()
        if self is TransferStatus.RETURNED:
            return returned()
