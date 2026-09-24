

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NoteReplyEntityNameTwo(enum.StrEnum):
    CUSTOMER_INVOICE = "customer_invoice"

    def visit(self, customer_invoice: typing.Callable[[], T_Result]) -> T_Result:
        if self is NoteReplyEntityNameTwo.CUSTOMER_INVOICE:
            return customer_invoice()
