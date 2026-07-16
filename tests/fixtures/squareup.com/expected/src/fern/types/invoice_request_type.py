

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InvoiceRequestType(enum.StrEnum):
    """
    Indicates the type of the payment request. For more information, see
    [Payment requests](https://developer.squareup.com/docs/invoices-api/overview#payment-requests).
    """

    BALANCE = "BALANCE"
    DEPOSIT = "DEPOSIT"
    INSTALLMENT = "INSTALLMENT"

    def visit(
        self,
        balance: typing.Callable[[], T_Result],
        deposit: typing.Callable[[], T_Result],
        installment: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InvoiceRequestType.BALANCE:
            return balance()
        if self is InvoiceRequestType.DEPOSIT:
            return deposit()
        if self is InvoiceRequestType.INSTALLMENT:
            return installment()
