

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CustomerInvoiceStatusZero(enum.StrEnum):
    UNPAID = "unpaid"

    def visit(self, unpaid: typing.Callable[[], T_Result]) -> T_Result:
        if self is CustomerInvoiceStatusZero.UNPAID:
            return unpaid()
