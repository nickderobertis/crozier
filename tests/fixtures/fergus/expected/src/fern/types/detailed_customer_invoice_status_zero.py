

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DetailedCustomerInvoiceStatusZero(enum.StrEnum):
    UNPAID = "unpaid"

    def visit(self, unpaid: typing.Callable[[], T_Result]) -> T_Result:
        if self is DetailedCustomerInvoiceStatusZero.UNPAID:
            return unpaid()
