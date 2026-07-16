

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionProduct(enum.StrEnum):
    """
    Indicates the Square product used to process a transaction.
    """

    REGISTER = "REGISTER"
    EXTERNAL_API = "EXTERNAL_API"
    BILLING = "BILLING"
    APPOINTMENTS = "APPOINTMENTS"
    INVOICES = "INVOICES"
    ONLINE_STORE = "ONLINE_STORE"
    PAYROLL = "PAYROLL"
    OTHER = "OTHER"

    def visit(
        self,
        register: typing.Callable[[], T_Result],
        external_api: typing.Callable[[], T_Result],
        billing: typing.Callable[[], T_Result],
        appointments: typing.Callable[[], T_Result],
        invoices: typing.Callable[[], T_Result],
        online_store: typing.Callable[[], T_Result],
        payroll: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransactionProduct.REGISTER:
            return register()
        if self is TransactionProduct.EXTERNAL_API:
            return external_api()
        if self is TransactionProduct.BILLING:
            return billing()
        if self is TransactionProduct.APPOINTMENTS:
            return appointments()
        if self is TransactionProduct.INVOICES:
            return invoices()
        if self is TransactionProduct.ONLINE_STORE:
            return online_store()
        if self is TransactionProduct.PAYROLL:
            return payroll()
        if self is TransactionProduct.OTHER:
            return other()
