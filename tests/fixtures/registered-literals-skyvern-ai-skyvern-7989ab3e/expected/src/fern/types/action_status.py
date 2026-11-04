

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActionStatus(enum.StrEnum):
    PENDING = "pending"
    SKIPPED = "skipped"
    FAILED = "failed"
    COMPLETED = "completed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        skipped: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActionStatus.PENDING:
            return pending()
        if self is ActionStatus.SKIPPED:
            return skipped()
        if self is ActionStatus.FAILED:
            return failed()
        if self is ActionStatus.COMPLETED:
            return completed()
