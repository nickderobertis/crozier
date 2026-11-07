

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExpandableExpensePaymentStatus(enum.StrEnum):
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
        if self is ExpandableExpensePaymentStatus.NOT_STARTED:
            return not_started()
        if self is ExpandableExpensePaymentStatus.PROCESSING:
            return processing()
        if self is ExpandableExpensePaymentStatus.CANCELED:
            return canceled()
        if self is ExpandableExpensePaymentStatus.DECLINED:
            return declined()
        if self is ExpandableExpensePaymentStatus.CLEARED:
            return cleared()
        if self is ExpandableExpensePaymentStatus.REFUNDING:
            return refunding()
        if self is ExpandableExpensePaymentStatus.REFUNDED:
            return refunded()
        if self is ExpandableExpensePaymentStatus.CASH_ADVANCE:
            return cash_advance()
        if self is ExpandableExpensePaymentStatus.CREDITED:
            return credited()
        if self is ExpandableExpensePaymentStatus.AWAITING_PAYMENT:
            return awaiting_payment()
        if self is ExpandableExpensePaymentStatus.SCHEDULED:
            return scheduled()
