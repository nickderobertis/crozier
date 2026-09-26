

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocumentsList200ResponseDocumentsItemState(enum.StrEnum):
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
        if self is DocumentsList200ResponseDocumentsItemState.PENDING:
            return pending()
        if self is DocumentsList200ResponseDocumentsItemState.READY:
            return ready()
        if self is DocumentsList200ResponseDocumentsItemState.FAILED:
            return failed()
        if self is DocumentsList200ResponseDocumentsItemState.DELETING:
            return deleting()
