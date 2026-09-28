

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V2UploadBackedTableImportStatus(enum.StrEnum):
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
        if self is V2UploadBackedTableImportStatus.UPLOADING:
            return uploading()
        if self is V2UploadBackedTableImportStatus.PROCESSING:
            return processing()
        if self is V2UploadBackedTableImportStatus.COMPLETED:
            return completed()
        if self is V2UploadBackedTableImportStatus.FAILED:
            return failed()
        if self is V2UploadBackedTableImportStatus.CANCELED:
            return canceled()
        if self is V2UploadBackedTableImportStatus.EXPIRED:
            return expired()
