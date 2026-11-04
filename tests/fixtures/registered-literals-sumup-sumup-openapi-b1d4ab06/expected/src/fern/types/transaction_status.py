

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionStatus(enum.StrEnum):
    """
    Current status of the transaction.

    - `PENDING`: The transaction has been created but its final outcome is not known yet.
    - `SUCCESSFUL`: The transaction completed successfully.
    - `CANCELLED`: The transaction was cancelled or otherwise reversed before completion.
    - `FAILED`: The transaction attempt did not complete successfully.
    - `REFUNDED`: The transaction was refunded in full or in part.
    """

    SUCCESSFUL = "SUCCESSFUL"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    REFUNDED = "REFUNDED"

    def visit(
        self,
        successful: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        refunded: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransactionStatus.SUCCESSFUL:
            return successful()
        if self is TransactionStatus.CANCELLED:
            return cancelled()
        if self is TransactionStatus.FAILED:
            return failed()
        if self is TransactionStatus.PENDING:
            return pending()
        if self is TransactionStatus.REFUNDED:
            return refunded()
