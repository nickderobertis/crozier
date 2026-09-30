

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CourseChapterGenerationStatus(enum.StrEnum):
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
        if self is CourseChapterGenerationStatus.COMPLETED:
            return completed()
        if self is CourseChapterGenerationStatus.FAILED:
            return failed()
        if self is CourseChapterGenerationStatus.PENDING:
            return pending()
        if self is CourseChapterGenerationStatus.RUNNING:
            return running()
