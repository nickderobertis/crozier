

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionType(enum.StrEnum):
    PURCHASE = "purchase"
    REBILL = "rebill"
    REFUND = "refund"
    FAILED_REBILL = "failed_rebill"
    CANCELLED = "cancelled"
    PENDING = "pending"

    def visit(
        self,
        purchase: typing.Callable[[], T_Result],
        rebill: typing.Callable[[], T_Result],
        refund: typing.Callable[[], T_Result],
        failed_rebill: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransactionType.PURCHASE:
            return purchase()
        if self is TransactionType.REBILL:
            return rebill()
        if self is TransactionType.REFUND:
            return refund()
        if self is TransactionType.FAILED_REBILL:
            return failed_rebill()
        if self is TransactionType.CANCELLED:
            return cancelled()
        if self is TransactionType.PENDING:
            return pending()
