

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExpensePaymentStatus(enum.StrEnum):
    NOT_STARTED = "NOT_STARTED"
    PROCESSING = "PROCESSING"
    CANCELED = "CANCELED"
    DECLINED = "DECLINED"
    CLEARED = "CLEARED"
    REFUNDING = "REFUNDING"
    REFUNDED = "REFUNDED"
    CASH_ADVANCE = "CASH_ADVANCE"
    CREDITED = "CREDITED"
    AWAITING_PAYMENT = "AWAITING_PAYMENT"
    SCHEDULED = "SCHEDULED"

    def visit(
        self,
        not_started: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        declined: typing.Callable[[], T_Result],
        cleared: typing.Callable[[], T_Result],
        refunding: typing.Callable[[], T_Result],
        refunded: typing.Callable[[], T_Result],
        cash_advance: typing.Callable[[], T_Result],
        credited: typing.Callable[[], T_Result],
        awaiting_payment: typing.Callable[[], T_Result],
        scheduled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExpensePaymentStatus.NOT_STARTED:
            return not_started()
        if self is ExpensePaymentStatus.PROCESSING:
            return processing()
        if self is ExpensePaymentStatus.CANCELED:
            return canceled()
        if self is ExpensePaymentStatus.DECLINED:
            return declined()
        if self is ExpensePaymentStatus.CLEARED:
            return cleared()
        if self is ExpensePaymentStatus.REFUNDING:
            return refunding()
        if self is ExpensePaymentStatus.REFUNDED:
            return refunded()
        if self is ExpensePaymentStatus.CASH_ADVANCE:
            return cash_advance()
        if self is ExpensePaymentStatus.CREDITED:
            return credited()
        if self is ExpensePaymentStatus.AWAITING_PAYMENT:
            return awaiting_payment()
        if self is ExpensePaymentStatus.SCHEDULED:
            return scheduled()
