

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChapterResourceGenerationStatus(enum.StrEnum):
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
        if self is ChapterResourceGenerationStatus.COMPLETED:
            return completed()
        if self is ChapterResourceGenerationStatus.FAILED:
            return failed()
        if self is ChapterResourceGenerationStatus.PENDING:
            return pending()
        if self is ChapterResourceGenerationStatus.RUNNING:
            return running()
