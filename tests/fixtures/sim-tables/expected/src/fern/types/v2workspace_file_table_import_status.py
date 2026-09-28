

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V2WorkspaceFileTableImportStatus(enum.StrEnum):
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
        if self is V2WorkspaceFileTableImportStatus.UPLOADING:
            return uploading()
        if self is V2WorkspaceFileTableImportStatus.PROCESSING:
            return processing()
        if self is V2WorkspaceFileTableImportStatus.COMPLETED:
            return completed()
        if self is V2WorkspaceFileTableImportStatus.FAILED:
            return failed()
        if self is V2WorkspaceFileTableImportStatus.CANCELED:
            return canceled()
        if self is V2WorkspaceFileTableImportStatus.EXPIRED:
            return expired()
