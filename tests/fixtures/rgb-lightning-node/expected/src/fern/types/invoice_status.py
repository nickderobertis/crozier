

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InvoiceStatus(enum.StrEnum):
    PENDING = "Pending"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    EXPIRED = "Expired"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InvoiceStatus.PENDING:
            return pending()
        if self is InvoiceStatus.SUCCEEDED:
            return succeeded()
        if self is InvoiceStatus.FAILED:
            return failed()
        if self is InvoiceStatus.EXPIRED:
            return expired()
