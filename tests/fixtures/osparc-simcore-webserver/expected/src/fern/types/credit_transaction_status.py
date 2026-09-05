

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreditTransactionStatus(enum.StrEnum):
    PENDING = "PENDING"
    BILLED = "BILLED"
    IN_DEBT = "IN_DEBT"
    NOT_BILLED = "NOT_BILLED"
    REQUIRES_MANUAL_REVIEW = "REQUIRES_MANUAL_REVIEW"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        billed: typing.Callable[[], T_Result],
        in_debt: typing.Callable[[], T_Result],
        not_billed: typing.Callable[[], T_Result],
        requires_manual_review: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreditTransactionStatus.PENDING:
            return pending()
        if self is CreditTransactionStatus.BILLED:
            return billed()
        if self is CreditTransactionStatus.IN_DEBT:
            return in_debt()
        if self is CreditTransactionStatus.NOT_BILLED:
            return not_billed()
        if self is CreditTransactionStatus.REQUIRES_MANUAL_REVIEW:
            return requires_manual_review()
