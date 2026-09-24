

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CustomerInvoiceStatusThree(enum.StrEnum):
    PAID_DISPUTED = "paidDisputed"

    def visit(self, paid_disputed: typing.Callable[[], T_Result]) -> T_Result:
        if self is CustomerInvoiceStatusThree.PAID_DISPUTED:
            return paid_disputed()
