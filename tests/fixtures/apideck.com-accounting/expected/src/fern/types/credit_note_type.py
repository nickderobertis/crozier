

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreditNoteType(enum.StrEnum):
    """
    Type of payment
    """

    ACCOUNTS_RECEIVABLE_CREDIT = "accounts_receivable_credit"
    ACCOUNTS_PAYABLE_CREDIT = "accounts_payable_credit"

    def visit(
        self,
        accounts_receivable_credit: typing.Callable[[], T_Result],
        accounts_payable_credit: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreditNoteType.ACCOUNTS_RECEIVABLE_CREDIT:
            return accounts_receivable_credit()
        if self is CreditNoteType.ACCOUNTS_PAYABLE_CREDIT:
            return accounts_payable_credit()
