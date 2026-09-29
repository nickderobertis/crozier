

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LessonQuestionStatus(enum.StrEnum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LessonQuestionStatus.PENDING:
            return pending()
        if self is LessonQuestionStatus.RUNNING:
            return running()
        if self is LessonQuestionStatus.COMPLETED:
            return completed()
        if self is LessonQuestionStatus.FAILED:
            return failed()
