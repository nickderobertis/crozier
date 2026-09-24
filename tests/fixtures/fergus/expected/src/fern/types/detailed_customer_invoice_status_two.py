

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DetailedCustomerInvoiceStatusTwo(enum.StrEnum):
    VOIDED = "voided"

    def visit(self, voided: typing.Callable[[], T_Result]) -> T_Result:
        if self is DetailedCustomerInvoiceStatusTwo.VOIDED:
            return voided()
