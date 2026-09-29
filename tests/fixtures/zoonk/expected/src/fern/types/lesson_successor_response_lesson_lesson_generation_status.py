

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LessonSuccessorResponseLessonLessonGenerationStatus(enum.StrEnum):
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
        if self is LessonSuccessorResponseLessonLessonGenerationStatus.COMPLETED:
            return completed()
        if self is LessonSuccessorResponseLessonLessonGenerationStatus.FAILED:
            return failed()
        if self is LessonSuccessorResponseLessonLessonGenerationStatus.PENDING:
            return pending()
        if self is LessonSuccessorResponseLessonLessonGenerationStatus.RUNNING:
            return running()
