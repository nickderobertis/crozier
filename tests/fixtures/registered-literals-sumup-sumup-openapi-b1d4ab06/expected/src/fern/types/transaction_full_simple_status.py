

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionFullSimpleStatus(enum.StrEnum):
    """
    High-level status of the transaction from the merchant's perspective.

    - `PENDING`: The payment has been initiated and is still being processed. A final outcome is not available yet.
    - `SUCCESSFUL`: The payment was completed successfully.
    - `PAID_OUT`: The payment was completed successfully and the funds have already been included in a payout to the merchant.
    - `FAILED`: The payment did not complete successfully.
    - `CANCELLED`: The payment was cancelled or reversed and is no longer payable or payable to the merchant.
    - `CANCEL_FAILED`: An attempt to cancel or reverse the payment was not completed successfully.
    - `REFUNDED`: The payment was refunded in full or in part.
    - `REFUND_FAILED`: An attempt to refund the payment was not completed successfully.
    - `CHARGEBACK`: The payment was subject to a chargeback.
    - `NON_COLLECTION`: The amount could not be collected from the merchant after a chargeback or related adjustment.
    """

    SUCCESSFUL = "SUCCESSFUL"
    PAID_OUT = "PAID_OUT"
    CANCEL_FAILED = "CANCEL_FAILED"
    CANCELLED = "CANCELLED"
    CHARGEBACK = "CHARGEBACK"
    FAILED = "FAILED"
    REFUND_FAILED = "REFUND_FAILED"
    REFUNDED = "REFUNDED"
    NON_COLLECTION = "NON_COLLECTION"
    PENDING = "PENDING"

    def visit(
        self,
        successful: typing.Callable[[], T_Result],
        paid_out: typing.Callable[[], T_Result],
        cancel_failed: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        chargeback: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        refund_failed: typing.Callable[[], T_Result],
        refunded: typing.Callable[[], T_Result],
        non_collection: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransactionFullSimpleStatus.SUCCESSFUL:
            return successful()
        if self is TransactionFullSimpleStatus.PAID_OUT:
            return paid_out()
        if self is TransactionFullSimpleStatus.CANCEL_FAILED:
            return cancel_failed()
        if self is TransactionFullSimpleStatus.CANCELLED:
            return cancelled()
        if self is TransactionFullSimpleStatus.CHARGEBACK:
            return chargeback()
        if self is TransactionFullSimpleStatus.FAILED:
            return failed()
        if self is TransactionFullSimpleStatus.REFUND_FAILED:
            return refund_failed()
        if self is TransactionFullSimpleStatus.REFUNDED:
            return refunded()
        if self is TransactionFullSimpleStatus.NON_COLLECTION:
            return non_collection()
        if self is TransactionFullSimpleStatus.PENDING:
            return pending()
