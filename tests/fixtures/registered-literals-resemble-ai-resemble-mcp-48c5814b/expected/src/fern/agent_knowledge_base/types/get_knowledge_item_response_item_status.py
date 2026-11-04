

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetKnowledgeItemResponseItemStatus(enum.StrEnum):
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
        if self is GetKnowledgeItemResponseItemStatus.PENDING:
            return pending()
        if self is GetKnowledgeItemResponseItemStatus.PROCESSING:
            return processing()
        if self is GetKnowledgeItemResponseItemStatus.READY:
            return ready()
        if self is GetKnowledgeItemResponseItemStatus.FAILED:
            return failed()
