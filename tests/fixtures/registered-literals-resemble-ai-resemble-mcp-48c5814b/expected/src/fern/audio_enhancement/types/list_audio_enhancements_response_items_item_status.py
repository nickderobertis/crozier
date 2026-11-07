

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListAudioEnhancementsResponseItemsItemStatus(enum.StrEnum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListAudioEnhancementsResponseItemsItemStatus.PENDING:
            return pending()
        if self is ListAudioEnhancementsResponseItemsItemStatus.PROCESSING:
            return processing()
        if self is ListAudioEnhancementsResponseItemsItemStatus.COMPLETED:
            return completed()
        if self is ListAudioEnhancementsResponseItemsItemStatus.FAILED:
            return failed()
