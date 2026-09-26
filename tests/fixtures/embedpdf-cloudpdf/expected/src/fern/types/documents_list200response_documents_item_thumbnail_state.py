

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocumentsList200ResponseDocumentsItemThumbnailState(enum.StrEnum):
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
        if self is DocumentsList200ResponseDocumentsItemThumbnailState.PENDING:
            return pending()
        if self is DocumentsList200ResponseDocumentsItemThumbnailState.READY:
            return ready()
        if self is DocumentsList200ResponseDocumentsItemThumbnailState.LOCKED:
            return locked()
        if self is DocumentsList200ResponseDocumentsItemThumbnailState.FAILED:
            return failed()
