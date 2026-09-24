

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CustomerInvoiceStatusOne(enum.StrEnum):
    DRAFT = "draft"

    def visit(self, draft: typing.Callable[[], T_Result]) -> T_Result:
        if self is CustomerInvoiceStatusOne.DRAFT:
            return draft()
