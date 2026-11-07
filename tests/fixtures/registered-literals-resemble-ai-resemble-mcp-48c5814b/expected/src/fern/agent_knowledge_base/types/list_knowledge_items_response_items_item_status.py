

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListKnowledgeItemsResponseItemsItemStatus(enum.StrEnum):
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
        if self is ListKnowledgeItemsResponseItemsItemStatus.PENDING:
            return pending()
        if self is ListKnowledgeItemsResponseItemsItemStatus.PROCESSING:
            return processing()
        if self is ListKnowledgeItemsResponseItemsItemStatus.READY:
            return ready()
        if self is ListKnowledgeItemsResponseItemsItemStatus.FAILED:
            return failed()
