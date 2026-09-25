

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DetailedCustomerInvoiceStatusThree(enum.StrEnum):
    PAID_DISPUTED = "paidDisputed"

    def visit(self, paid_disputed: typing.Callable[[], T_Result]) -> T_Result:
        if self is DetailedCustomerInvoiceStatusThree.PAID_DISPUTED:
            return paid_disputed()
