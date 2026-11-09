

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InvoiceStatus(enum.StrEnum):
    PENDING = "pending"
    PAID = "paid"
    OVERDUE = "overdue"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        paid: typing.Callable[[], T_Result],
        overdue: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InvoiceStatus.PENDING:
            return pending()
        if self is InvoiceStatus.PAID:
            return paid()
        if self is InvoiceStatus.OVERDUE:
            return overdue()
