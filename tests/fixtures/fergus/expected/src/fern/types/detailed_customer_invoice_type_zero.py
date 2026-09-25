

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DetailedCustomerInvoiceTypeZero(enum.StrEnum):
    APPROVED = "approved"

    def visit(self, approved: typing.Callable[[], T_Result]) -> T_Result:
        if self is DetailedCustomerInvoiceTypeZero.APPROVED:
            return approved()
