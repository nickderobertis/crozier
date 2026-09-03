

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProcessStepResponseStatus(enum.StrEnum):
    COMPLETED = "completed"
    PENDING = "pending"
    FAILED = "failed"
    SKIPPED = "skipped"

    def visit(
        self,
        completed: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        skipped: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProcessStepResponseStatus.COMPLETED:
            return completed()
        if self is ProcessStepResponseStatus.PENDING:
            return pending()
        if self is ProcessStepResponseStatus.FAILED:
            return failed()
        if self is ProcessStepResponseStatus.SKIPPED:
            return skipped()
