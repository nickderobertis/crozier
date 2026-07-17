

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InvoiceCustomFieldPlacement(enum.StrEnum):
    """
    Indicates where to render a custom field on the Square-hosted invoice page and in emailed or PDF
    copies of the invoice.
    """

    ABOVE_LINE_ITEMS = "ABOVE_LINE_ITEMS"
    BELOW_LINE_ITEMS = "BELOW_LINE_ITEMS"

    def visit(
        self, above_line_items: typing.Callable[[], T_Result], below_line_items: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is InvoiceCustomFieldPlacement.ABOVE_LINE_ITEMS:
            return above_line_items()
        if self is InvoiceCustomFieldPlacement.BELOW_LINE_ITEMS:
            return below_line_items()
