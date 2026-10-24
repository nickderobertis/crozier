

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActionStatus(enum.StrEnum):
    REQUESTED = "requested"
    APPROVED = "approved"
    EXECUTING = "executing"
    EXECUTED = "executed"
    FAILED = "failed"
    REJECTED = "rejected"

    def visit(
        self,
        requested: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        executing: typing.Callable[[], T_Result],
        executed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActionStatus.REQUESTED:
            return requested()
        if self is ActionStatus.APPROVED:
            return approved()
        if self is ActionStatus.EXECUTING:
            return executing()
        if self is ActionStatus.EXECUTED:
            return executed()
        if self is ActionStatus.FAILED:
            return failed()
        if self is ActionStatus.REJECTED:
            return rejected()
