

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocumentsImportFrom202ResponseDocumentState(enum.StrEnum):
    PENDING = "pending"
    READY = "ready"
    FAILED = "failed"
    DELETING = "deleting"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        ready: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        deleting: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocumentsImportFrom202ResponseDocumentState.PENDING:
            return pending()
        if self is DocumentsImportFrom202ResponseDocumentState.READY:
            return ready()
        if self is DocumentsImportFrom202ResponseDocumentState.FAILED:
            return failed()
        if self is DocumentsImportFrom202ResponseDocumentState.DELETING:
            return deleting()
