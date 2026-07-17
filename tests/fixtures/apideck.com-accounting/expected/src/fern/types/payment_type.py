

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaymentType(enum.StrEnum):
    """
    Type of payment
    """

    ACCOUNTS_RECEIVABLE = "accounts_receivable"
    ACCOUNTS_PAYABLE = "accounts_payable"
    ACCOUNTS_RECEIVABLE_CREDIT = "accounts_receivable_credit"
    ACCOUNTS_PAYABLE_CREDIT = "accounts_payable_credit"
    ACCOUNTS_RECEIVABLE_OVERPAYMENT = "accounts_receivable_overpayment"
    ACCOUNTS_PAYABLE_OVERPAYMENT = "accounts_payable_overpayment"
    ACCOUNTS_RECEIVABLE_PREPAYMENT = "accounts_receivable_prepayment"
    ACCOUNTS_PAYABLE_PREPAYMENT = "accounts_payable_prepayment"

    def visit(
        self,
        accounts_receivable: typing.Callable[[], T_Result],
        accounts_payable: typing.Callable[[], T_Result],
        accounts_receivable_credit: typing.Callable[[], T_Result],
        accounts_payable_credit: typing.Callable[[], T_Result],
        accounts_receivable_overpayment: typing.Callable[[], T_Result],
        accounts_payable_overpayment: typing.Callable[[], T_Result],
        accounts_receivable_prepayment: typing.Callable[[], T_Result],
        accounts_payable_prepayment: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PaymentType.ACCOUNTS_RECEIVABLE:
            return accounts_receivable()
        if self is PaymentType.ACCOUNTS_PAYABLE:
            return accounts_payable()
        if self is PaymentType.ACCOUNTS_RECEIVABLE_CREDIT:
            return accounts_receivable_credit()
        if self is PaymentType.ACCOUNTS_PAYABLE_CREDIT:
            return accounts_payable_credit()
        if self is PaymentType.ACCOUNTS_RECEIVABLE_OVERPAYMENT:
            return accounts_receivable_overpayment()
        if self is PaymentType.ACCOUNTS_PAYABLE_OVERPAYMENT:
            return accounts_payable_overpayment()
        if self is PaymentType.ACCOUNTS_RECEIVABLE_PREPAYMENT:
            return accounts_receivable_prepayment()
        if self is PaymentType.ACCOUNTS_PAYABLE_PREPAYMENT:
            return accounts_payable_prepayment()
