

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CourseResourceGenerationStatus(enum.StrEnum):
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
        if self is CourseResourceGenerationStatus.COMPLETED:
            return completed()
        if self is CourseResourceGenerationStatus.FAILED:
            return failed()
        if self is CourseResourceGenerationStatus.PENDING:
            return pending()
        if self is CourseResourceGenerationStatus.RUNNING:
            return running()
