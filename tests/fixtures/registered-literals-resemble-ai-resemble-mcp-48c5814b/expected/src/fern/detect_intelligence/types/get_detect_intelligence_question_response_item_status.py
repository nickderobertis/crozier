

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetDetectIntelligenceQuestionResponseItemStatus(enum.StrEnum):
    """
    Current status of the question
    """

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
        if self is GetDetectIntelligenceQuestionResponseItemStatus.PENDING:
            return pending()
        if self is GetDetectIntelligenceQuestionResponseItemStatus.PROCESSING:
            return processing()
        if self is GetDetectIntelligenceQuestionResponseItemStatus.COMPLETED:
            return completed()
        if self is GetDetectIntelligenceQuestionResponseItemStatus.FAILED:
            return failed()
