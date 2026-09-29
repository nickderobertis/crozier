

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CoursePromptGenerationResponsePendingGenerationStatus(enum.StrEnum):
    COMPLETED = "completed"
    FAILED = "failed"
    PENDING = "pending"
    RUNNING = "running"

    def visit(
        self,
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CoursePromptGenerationResponsePendingGenerationStatus.COMPLETED:
            return completed()
        if self is CoursePromptGenerationResponsePendingGenerationStatus.FAILED:
            return failed()
        if self is CoursePromptGenerationResponsePendingGenerationStatus.PENDING:
            return pending()
        if self is CoursePromptGenerationResponsePendingGenerationStatus.RUNNING:
            return running()
