

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class InvoicePaymentReminderStatus(str, enum.Enum):
    """
    The status of a payment request reminder.
    """

    PENDING = "PENDING"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    SENT = "SENT"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        not_applicable: typing.Callable[[], T_Result],
        sent: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InvoicePaymentReminderStatus.PENDING:
            return pending()
        if self is InvoicePaymentReminderStatus.NOT_APPLICABLE:
            return not_applicable()
        if self is InvoicePaymentReminderStatus.SENT:
            return sent()
