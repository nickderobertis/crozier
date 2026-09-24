

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CustomerInvoiceStatusTwo(enum.StrEnum):
    VOIDED = "voided"

    def visit(self, voided: typing.Callable[[], T_Result]) -> T_Result:
        if self is CustomerInvoiceStatusTwo.VOIDED:
            return voided()
