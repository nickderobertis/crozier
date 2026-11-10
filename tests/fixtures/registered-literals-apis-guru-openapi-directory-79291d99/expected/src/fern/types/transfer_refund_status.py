

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransferRefundStatus(enum.StrEnum):
    """
    The status of the refund.

    `pending`: A new refund was created; it is in the pending state.
    `posted`: The refund has been successfully submitted to the payment network.
    `cancelled`: The refund was cancelled by the client.
    `failed`: The refund failed or was returned.
    """

    PENDING = "pending"
    POSTED = "posted"
    CANCELLED = "cancelled"
    FAILED = "failed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        posted: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransferRefundStatus.PENDING:
            return pending()
        if self is TransferRefundStatus.POSTED:
            return posted()
        if self is TransferRefundStatus.CANCELLED:
            return cancelled()
        if self is TransferRefundStatus.FAILED:
            return failed()
