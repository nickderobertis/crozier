

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DetailedCustomerInvoiceStatusFive(enum.StrEnum):
    PAID = "paid"

    def visit(self, paid: typing.Callable[[], T_Result]) -> T_Result:
        if self is DetailedCustomerInvoiceStatusFive.PAID:
            return paid()
