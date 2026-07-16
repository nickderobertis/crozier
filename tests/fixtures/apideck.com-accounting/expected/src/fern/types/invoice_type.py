

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InvoiceType(enum.StrEnum):
    """
    Invoice type
    """

    STANDARD = "standard"
    CREDIT = "credit"
    SERVICE = "service"
    PRODUCT = "product"
    SUPPLIER = "supplier"
    OTHER = "other"

    def visit(
        self,
        standard: typing.Callable[[], T_Result],
        credit: typing.Callable[[], T_Result],
        service: typing.Callable[[], T_Result],
        product: typing.Callable[[], T_Result],
        supplier: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InvoiceType.STANDARD:
            return standard()
        if self is InvoiceType.CREDIT:
            return credit()
        if self is InvoiceType.SERVICE:
            return service()
        if self is InvoiceType.PRODUCT:
            return product()
        if self is InvoiceType.SUPPLIER:
            return supplier()
        if self is InvoiceType.OTHER:
            return other()
