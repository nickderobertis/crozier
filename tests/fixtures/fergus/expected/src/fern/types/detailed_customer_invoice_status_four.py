

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DetailedCustomerInvoiceStatusFour(enum.StrEnum):
    UNPAID_DISPUTED = "unpaidDisputed"

    def visit(self, unpaid_disputed: typing.Callable[[], T_Result]) -> T_Result:
        if self is DetailedCustomerInvoiceStatusFour.UNPAID_DISPUTED:
            return unpaid_disputed()
