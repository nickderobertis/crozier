

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocumentsInit200ResponseDedupedDocumentThumbnailState(enum.StrEnum):
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
        if self is DocumentsInit200ResponseDedupedDocumentThumbnailState.PENDING:
            return pending()
        if self is DocumentsInit200ResponseDedupedDocumentThumbnailState.READY:
            return ready()
        if self is DocumentsInit200ResponseDedupedDocumentThumbnailState.LOCKED:
            return locked()
        if self is DocumentsInit200ResponseDedupedDocumentThumbnailState.FAILED:
            return failed()
