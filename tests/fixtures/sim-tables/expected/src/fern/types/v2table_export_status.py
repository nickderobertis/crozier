

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V2TableExportStatus(enum.StrEnum):
    """
    Current export lifecycle state.
    """

    QUEUED = "queued"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELED = "canceled"

    def visit(
        self,
        queued: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V2TableExportStatus.QUEUED:
            return queued()
        if self is V2TableExportStatus.PROCESSING:
            return processing()
        if self is V2TableExportStatus.COMPLETED:
            return completed()
        if self is V2TableExportStatus.FAILED:
            return failed()
        if self is V2TableExportStatus.CANCELED:
            return canceled()
