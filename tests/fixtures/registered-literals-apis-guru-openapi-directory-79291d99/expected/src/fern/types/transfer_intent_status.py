

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransferIntentStatus(enum.StrEnum):
    """
    The status of the transfer intent.

    `PENDING`: The transfer intent is pending.
    `SUCCEEDED`: The transfer intent was successfully created.
    `FAILED`: The transfer intent was unable to be created.
    """

    PENDING = "PENDING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransferIntentStatus.PENDING:
            return pending()
        if self is TransferIntentStatus.SUCCEEDED:
            return succeeded()
        if self is TransferIntentStatus.FAILED:
            return failed()
