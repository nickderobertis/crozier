

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InvoiceStatus(enum.StrEnum):
    """
    Invoice status
    """

    DRAFT = "draft"
    SUBMITTED = "submitted"
    AUTHORISED = "authorised"
    PARTIALLY_PAID = "partially_paid"
    PAID = "paid"
    VOID = "void"
    CREDIT = "credit"
    DELETED = "deleted"

    def visit(
        self,
        draft: typing.Callable[[], T_Result],
        submitted: typing.Callable[[], T_Result],
        authorised: typing.Callable[[], T_Result],
        partially_paid: typing.Callable[[], T_Result],
        paid: typing.Callable[[], T_Result],
        void: typing.Callable[[], T_Result],
        credit: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InvoiceStatus.DRAFT:
            return draft()
        if self is InvoiceStatus.SUBMITTED:
            return submitted()
        if self is InvoiceStatus.AUTHORISED:
            return authorised()
        if self is InvoiceStatus.PARTIALLY_PAID:
            return partially_paid()
        if self is InvoiceStatus.PAID:
            return paid()
        if self is InvoiceStatus.VOID:
            return void()
        if self is InvoiceStatus.CREDIT:
            return credit()
        if self is InvoiceStatus.DELETED:
            return deleted()
