

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UploadStatus(enum.StrEnum):
    PENDING = "pending"
    UPLOADING = "uploading"
    FINALIZING = "finalizing"
    FINALIZED = "finalized"
    FAILED = "failed"
    EXPIRED = "expired"
    CANCELLED = "cancelled"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        uploading: typing.Callable[[], T_Result],
        finalizing: typing.Callable[[], T_Result],
        finalized: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UploadStatus.PENDING:
            return pending()
        if self is UploadStatus.UPLOADING:
            return uploading()
        if self is UploadStatus.FINALIZING:
            return finalizing()
        if self is UploadStatus.FINALIZED:
            return finalized()
        if self is UploadStatus.FAILED:
            return failed()
        if self is UploadStatus.EXPIRED:
            return expired()
        if self is UploadStatus.CANCELLED:
            return cancelled()
