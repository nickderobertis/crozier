

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V2TableImportStatus(enum.StrEnum):
    """
    Current import lifecycle state.
    """

    UPLOADING = "uploading"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELED = "canceled"
    EXPIRED = "expired"

    def visit(
        self,
        uploading: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V2TableImportStatus.UPLOADING:
            return uploading()
        if self is V2TableImportStatus.PROCESSING:
            return processing()
        if self is V2TableImportStatus.COMPLETED:
            return completed()
        if self is V2TableImportStatus.FAILED:
            return failed()
        if self is V2TableImportStatus.CANCELED:
            return canceled()
        if self is V2TableImportStatus.EXPIRED:
            return expired()
