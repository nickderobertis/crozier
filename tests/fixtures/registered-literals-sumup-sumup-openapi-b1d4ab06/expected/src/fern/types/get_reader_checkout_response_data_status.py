

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetReaderCheckoutResponseDataStatus(enum.StrEnum):
    """
    Current status of the checkout
    """

    PENDING = "pending"
    SUCCESSFUL = "successful"
    FAILED = "failed"
    CANCELLED = "cancelled"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        successful: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetReaderCheckoutResponseDataStatus.PENDING:
            return pending()
        if self is GetReaderCheckoutResponseDataStatus.SUCCESSFUL:
            return successful()
        if self is GetReaderCheckoutResponseDataStatus.FAILED:
            return failed()
        if self is GetReaderCheckoutResponseDataStatus.CANCELLED:
            return cancelled()
