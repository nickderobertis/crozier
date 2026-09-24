

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DetailedCustomerInvoiceStatusOne(enum.StrEnum):
    DRAFT = "draft"

    def visit(self, draft: typing.Callable[[], T_Result]) -> T_Result:
        if self is DetailedCustomerInvoiceStatusOne.DRAFT:
            return draft()
