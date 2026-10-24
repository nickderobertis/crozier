

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProposalExecutionStatus(enum.StrEnum):
    PENDING = "pending"
    EXECUTING = "executing"
    EXECUTED = "executed"
    FAILED = "failed"
    BLOCKED = "blocked"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        executing: typing.Callable[[], T_Result],
        executed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        blocked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProposalExecutionStatus.PENDING:
            return pending()
        if self is ProposalExecutionStatus.EXECUTING:
            return executing()
        if self is ProposalExecutionStatus.EXECUTED:
            return executed()
        if self is ProposalExecutionStatus.FAILED:
            return failed()
        if self is ProposalExecutionStatus.BLOCKED:
            return blocked()
