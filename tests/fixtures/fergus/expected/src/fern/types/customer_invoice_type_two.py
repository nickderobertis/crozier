

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CustomerInvoiceTypeTwo(enum.StrEnum):
    DRAFT = "draft"

    def visit(self, draft: typing.Callable[[], T_Result]) -> T_Result:
        if self is CustomerInvoiceTypeTwo.DRAFT:
            return draft()
