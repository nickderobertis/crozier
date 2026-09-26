

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocumentsImportFrom200ResponseDocumentThumbnailState(enum.StrEnum):
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
        if self is DocumentsImportFrom200ResponseDocumentThumbnailState.PENDING:
            return pending()
        if self is DocumentsImportFrom200ResponseDocumentThumbnailState.READY:
            return ready()
        if self is DocumentsImportFrom200ResponseDocumentThumbnailState.LOCKED:
            return locked()
        if self is DocumentsImportFrom200ResponseDocumentThumbnailState.FAILED:
            return failed()
