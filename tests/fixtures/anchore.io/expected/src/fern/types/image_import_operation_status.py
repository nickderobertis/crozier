

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ImageImportOperationStatus(enum.StrEnum):
    PENDING = "pending"
    QUEUED = "queued"
    PROCESSING = "processing"
    COMPLETE = "complete"
    FAILED = "failed"
    EXPIRED = "expired"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        queued: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
        complete: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ImageImportOperationStatus.PENDING:
            return pending()
        if self is ImageImportOperationStatus.QUEUED:
            return queued()
        if self is ImageImportOperationStatus.PROCESSING:
            return processing()
        if self is ImageImportOperationStatus.COMPLETE:
            return complete()
        if self is ImageImportOperationStatus.FAILED:
            return failed()
        if self is ImageImportOperationStatus.EXPIRED:
            return expired()
