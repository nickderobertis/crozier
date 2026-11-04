

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionEventStatus(enum.StrEnum):
    """
    Status of the transaction event.

    Not every value is used for every event type.

    - `PENDING`: The event has been created but is not final yet. Used for events that are still being processed and whose final outcome is not known yet.
    - `SCHEDULED`: The event is planned for a future payout cycle but has not been executed yet. This applies to payout events before money is actually sent out.
    - `RECONCILED`: The underlying payment has been matched with settlement data and is ready to continue through payout processing, but the funds have not been paid out yet. This applies to payout events.
    - `PAID_OUT`: The payout event has been completed and the funds were included in a merchant payout.
    - `REFUNDED`: A refund event has been accepted and recorded in the refund flow. This is the status returned for refund events once the transaction amount is being or has been returned to the payer.
    - `SUCCESSFUL`: The event completed successfully. Use this as the generic terminal success status for event types that do not expose a more specific business outcome such as `PAID_OUT` or `REFUNDED`.
    - `FAILED`: The event could not be completed. Typical examples are a payout that could not be executed or an event that was rejected during processing.
    """

    FAILED = "FAILED"
    PAID_OUT = "PAID_OUT"
    PENDING = "PENDING"
    RECONCILED = "RECONCILED"
    REFUNDED = "REFUNDED"
    SCHEDULED = "SCHEDULED"
    SUCCESSFUL = "SUCCESSFUL"

    def visit(
        self,
        failed: typing.Callable[[], T_Result],
        paid_out: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        reconciled: typing.Callable[[], T_Result],
        refunded: typing.Callable[[], T_Result],
        scheduled: typing.Callable[[], T_Result],
        successful: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransactionEventStatus.FAILED:
            return failed()
        if self is TransactionEventStatus.PAID_OUT:
            return paid_out()
        if self is TransactionEventStatus.PENDING:
            return pending()
        if self is TransactionEventStatus.RECONCILED:
            return reconciled()
        if self is TransactionEventStatus.REFUNDED:
            return refunded()
        if self is TransactionEventStatus.SCHEDULED:
            return scheduled()
        if self is TransactionEventStatus.SUCCESSFUL:
            return successful()
