

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CustomerInvoiceTypeZero(enum.StrEnum):
    APPROVED = "approved"

    def visit(self, approved: typing.Callable[[], T_Result]) -> T_Result:
        if self is CustomerInvoiceTypeZero.APPROVED:
            return approved()
