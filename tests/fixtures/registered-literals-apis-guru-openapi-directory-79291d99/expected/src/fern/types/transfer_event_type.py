

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransferEventType(enum.StrEnum):
    """
    The type of event that this transfer represents.

    `pending`: A new transfer was created; it is in the pending state.

    `cancelled`: The transfer was cancelled by the client.

    `failed`: The transfer failed, no funds were moved.

    `posted`: The transfer has been successfully submitted to the payment network.

    `settled`: Credits are available to be withdrawn or debits have been deducted from the Plaid linked account.

    `returned`: A posted transfer was returned.

    `swept`: The transfer was swept to / from the sweep account.

    `swept_settled`: Credits are available to be withdrawn or debits have been deducted from the customer’s business checking account.

    `return_swept`: Due to the transfer being returned, funds were pulled from or pushed back to the sweep account.
    """

    PENDING = "pending"
    CANCELLED = "cancelled"
    FAILED = "failed"
    POSTED = "posted"
    SETTLED = "settled"
    RETURNED = "returned"
    SWEPT = "swept"
    SWEPT_SETTLED = "swept_settled"
    RETURN_SWEPT = "return_swept"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        posted: typing.Callable[[], T_Result],
        settled: typing.Callable[[], T_Result],
        returned: typing.Callable[[], T_Result],
        swept: typing.Callable[[], T_Result],
        swept_settled: typing.Callable[[], T_Result],
        return_swept: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransferEventType.PENDING:
            return pending()
        if self is TransferEventType.CANCELLED:
            return cancelled()
        if self is TransferEventType.FAILED:
            return failed()
        if self is TransferEventType.POSTED:
            return posted()
        if self is TransferEventType.SETTLED:
            return settled()
        if self is TransferEventType.RETURNED:
            return returned()
        if self is TransferEventType.SWEPT:
            return swept()
        if self is TransferEventType.SWEPT_SETTLED:
            return swept_settled()
        if self is TransferEventType.RETURN_SWEPT:
            return return_swept()
