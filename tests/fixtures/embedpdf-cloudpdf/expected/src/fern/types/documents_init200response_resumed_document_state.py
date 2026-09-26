

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocumentsInit200ResponseResumedDocumentState(enum.StrEnum):
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
        if self is DocumentsInit200ResponseResumedDocumentState.PENDING:
            return pending()
        if self is DocumentsInit200ResponseResumedDocumentState.READY:
            return ready()
        if self is DocumentsInit200ResponseResumedDocumentState.FAILED:
            return failed()
        if self is DocumentsInit200ResponseResumedDocumentState.DELETING:
            return deleting()
