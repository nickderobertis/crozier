

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocumentsCommit200ResponseDocumentThumbnailState(enum.StrEnum):
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
        if self is DocumentsCommit200ResponseDocumentThumbnailState.PENDING:
            return pending()
        if self is DocumentsCommit200ResponseDocumentThumbnailState.READY:
            return ready()
        if self is DocumentsCommit200ResponseDocumentThumbnailState.LOCKED:
            return locked()
        if self is DocumentsCommit200ResponseDocumentThumbnailState.FAILED:
            return failed()
