

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class InvoiceStatus(str, enum.Enum):
    """
    Indicates the status of an invoice.
    """

    DRAFT = "DRAFT"
    UNPAID = "UNPAID"
    SCHEDULED = "SCHEDULED"
    PARTIALLY_PAID = "PARTIALLY_PAID"
    PAID = "PAID"
    PARTIALLY_REFUNDED = "PARTIALLY_REFUNDED"
    REFUNDED = "REFUNDED"
    CANCELED = "CANCELED"
    FAILED = "FAILED"
    PAYMENT_PENDING = "PAYMENT_PENDING"

    def visit(
        self,
        draft: typing.Callable[[], T_Result],
        unpaid: typing.Callable[[], T_Result],
        scheduled: typing.Callable[[], T_Result],
        partially_paid: typing.Callable[[], T_Result],
        paid: typing.Callable[[], T_Result],
        partially_refunded: typing.Callable[[], T_Result],
        refunded: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        payment_pending: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InvoiceStatus.DRAFT:
            return draft()
        if self is InvoiceStatus.UNPAID:
            return unpaid()
        if self is InvoiceStatus.SCHEDULED:
            return scheduled()
        if self is InvoiceStatus.PARTIALLY_PAID:
            return partially_paid()
        if self is InvoiceStatus.PAID:
            return paid()
        if self is InvoiceStatus.PARTIALLY_REFUNDED:
            return partially_refunded()
        if self is InvoiceStatus.REFUNDED:
            return refunded()
        if self is InvoiceStatus.CANCELED:
            return canceled()
        if self is InvoiceStatus.FAILED:
            return failed()
        if self is InvoiceStatus.PAYMENT_PENDING:
            return payment_pending()
