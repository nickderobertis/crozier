

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaymentTransactionCompletedStatus(enum.StrEnum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    CANCELED = "CANCELED"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        success: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PaymentTransactionCompletedStatus.PENDING:
            return pending()
        if self is PaymentTransactionCompletedStatus.SUCCESS:
            return success()
        if self is PaymentTransactionCompletedStatus.FAILED:
            return failed()
        if self is PaymentTransactionCompletedStatus.CANCELED:
            return canceled()
