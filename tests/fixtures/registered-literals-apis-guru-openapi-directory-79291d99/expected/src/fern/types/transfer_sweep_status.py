

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransferSweepStatus(enum.StrEnum):
    """
    The status of the sweep for the transfer.

    `unswept`: The transfer hasn't been swept yet.
    `swept`: The transfer was swept to the sweep account.
    `swept_settled`: Credits are available to be withdrawn or debits have been deducted from the customer’s business checking account.
    `return_swept`: The transfer was returned, funds were pulled back or pushed back to the sweep account.
    `null`: The transfer will never be swept (e.g. if the transfer is cancelled or returned before being swept)
    """

    UNSWEPT = "unswept"
    SWEPT = "swept"
    SWEPT_SETTLED = "swept_settled"
    RETURN_SWEPT = "return_swept"

    def visit(
        self,
        unswept: typing.Callable[[], T_Result],
        swept: typing.Callable[[], T_Result],
        swept_settled: typing.Callable[[], T_Result],
        return_swept: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransferSweepStatus.UNSWEPT:
            return unswept()
        if self is TransferSweepStatus.SWEPT:
            return swept()
        if self is TransferSweepStatus.SWEPT_SETTLED:
            return swept_settled()
        if self is TransferSweepStatus.RETURN_SWEPT:
            return return_swept()
