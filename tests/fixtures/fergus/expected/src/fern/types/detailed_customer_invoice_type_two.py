

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DetailedCustomerInvoiceTypeTwo(enum.StrEnum):
    DRAFT = "draft"

    def visit(self, draft: typing.Callable[[], T_Result]) -> T_Result:
        if self is DetailedCustomerInvoiceTypeTwo.DRAFT:
            return draft()
