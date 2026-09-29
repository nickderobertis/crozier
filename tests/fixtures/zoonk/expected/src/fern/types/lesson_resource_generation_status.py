

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LessonResourceGenerationStatus(enum.StrEnum):
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
        if self is LessonResourceGenerationStatus.COMPLETED:
            return completed()
        if self is LessonResourceGenerationStatus.FAILED:
            return failed()
        if self is LessonResourceGenerationStatus.PENDING:
            return pending()
        if self is LessonResourceGenerationStatus.RUNNING:
            return running()
