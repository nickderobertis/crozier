

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InvoicesSortBy(enum.StrEnum):
    """
    The field on which to sort the Invoices
    """

    UPDATED_AT = "updated_at"

    def visit(self, updated_at: typing.Callable[[], T_Result]) -> T_Result:
        if self is InvoicesSortBy.UPDATED_AT:
            return updated_at()
