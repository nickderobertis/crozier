

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocumentsInit200ResponseCreatedDocumentThumbnailState(enum.StrEnum):
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
        if self is DocumentsInit200ResponseCreatedDocumentThumbnailState.PENDING:
            return pending()
        if self is DocumentsInit200ResponseCreatedDocumentThumbnailState.READY:
            return ready()
        if self is DocumentsInit200ResponseCreatedDocumentThumbnailState.LOCKED:
            return locked()
        if self is DocumentsInit200ResponseCreatedDocumentThumbnailState.FAILED:
            return failed()
