

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CustomerInvoiceStatusFour(enum.StrEnum):
    UNPAID_DISPUTED = "unpaidDisputed"

    def visit(self, unpaid_disputed: typing.Callable[[], T_Result]) -> T_Result:
        if self is CustomerInvoiceStatusFour.UNPAID_DISPUTED:
            return unpaid_disputed()
