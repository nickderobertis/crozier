

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UploadSummaryClearingStatus(enum.StrEnum):
    """
    Upload is clearing status.
    """

    OPEN = "Open"
    IN_PROGRESS = "InProgress"
    CLOSED = "Closed"
    REJECTED = "Rejected"

    def visit(
        self,
        open: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        closed: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UploadSummaryClearingStatus.OPEN:
            return open()
        if self is UploadSummaryClearingStatus.IN_PROGRESS:
            return in_progress()
        if self is UploadSummaryClearingStatus.CLOSED:
            return closed()
        if self is UploadSummaryClearingStatus.REJECTED:
            return rejected()
