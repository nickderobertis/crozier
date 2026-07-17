

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InvoiceSortField(enum.StrEnum):
    """
    The field to use for sorting.
    """

    INVOICE_SORT_DATE = "INVOICE_SORT_DATE"

    def visit(self, invoice_sort_date: typing.Callable[[], T_Result]) -> T_Result:
        if self is InvoiceSortField.INVOICE_SORT_DATE:
            return invoice_sort_date()
