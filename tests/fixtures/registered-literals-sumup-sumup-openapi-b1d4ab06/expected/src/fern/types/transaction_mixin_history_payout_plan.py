

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionMixinHistoryPayoutPlan(enum.StrEnum):
    """
    Payout plan of the registered user at the time when the transaction was made.
    """

    SINGLE_PAYMENT = "SINGLE_PAYMENT"
    TRUE_INSTALLMENT = "TRUE_INSTALLMENT"
    ACCELERATED_INSTALLMENT = "ACCELERATED_INSTALLMENT"

    def visit(
        self,
        single_payment: typing.Callable[[], T_Result],
        true_installment: typing.Callable[[], T_Result],
        accelerated_installment: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransactionMixinHistoryPayoutPlan.SINGLE_PAYMENT:
            return single_payment()
        if self is TransactionMixinHistoryPayoutPlan.TRUE_INSTALLMENT:
            return true_installment()
        if self is TransactionMixinHistoryPayoutPlan.ACCELERATED_INSTALLMENT:
            return accelerated_installment()
