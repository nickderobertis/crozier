

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CourseEditionResponseGenerationGenerationStatus(enum.StrEnum):
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
        if self is CourseEditionResponseGenerationGenerationStatus.COMPLETED:
            return completed()
        if self is CourseEditionResponseGenerationGenerationStatus.FAILED:
            return failed()
        if self is CourseEditionResponseGenerationGenerationStatus.PENDING:
            return pending()
        if self is CourseEditionResponseGenerationGenerationStatus.RUNNING:
            return running()
