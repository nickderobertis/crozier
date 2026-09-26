

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocumentsImportFrom202ResponseDocumentThumbnailState(enum.StrEnum):
    PENDING = "pending"
    READY = "ready"
    LOCKED = "locked"
    FAILED = "failed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        ready: typing.Callable[[], T_Result],
        locked: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocumentsImportFrom202ResponseDocumentThumbnailState.PENDING:
            return pending()
        if self is DocumentsImportFrom202ResponseDocumentThumbnailState.READY:
            return ready()
        if self is DocumentsImportFrom202ResponseDocumentThumbnailState.LOCKED:
            return locked()
        if self is DocumentsImportFrom202ResponseDocumentThumbnailState.FAILED:
            return failed()
