

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListKnowledgeItemsRequestStatus(enum.StrEnum):
    PENDING = "pending"
    PROCESSING = "processing"
    READY = "ready"
    FAILED = "failed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
        ready: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListKnowledgeItemsRequestStatus.PENDING:
            return pending()
        if self is ListKnowledgeItemsRequestStatus.PROCESSING:
            return processing()
        if self is ListKnowledgeItemsRequestStatus.READY:
            return ready()
        if self is ListKnowledgeItemsRequestStatus.FAILED:
            return failed()
