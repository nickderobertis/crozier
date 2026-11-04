

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WorkflowRetryRuleStatus(enum.StrEnum):
    """
    Terminal status that triggers a retry rule; canceled is accepted for forward compatibility, but a canceled run never retries in the current runtime, including explicit API/UI cancels.
    """

    COMPLETED = "completed"
    FAILED = "failed"
    TERMINATED = "terminated"
    CANCELED = "canceled"
    TIMED_OUT = "timed_out"

    def visit(
        self,
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        terminated: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        timed_out: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WorkflowRetryRuleStatus.COMPLETED:
            return completed()
        if self is WorkflowRetryRuleStatus.FAILED:
            return failed()
        if self is WorkflowRetryRuleStatus.TERMINATED:
            return terminated()
        if self is WorkflowRetryRuleStatus.CANCELED:
            return canceled()
        if self is WorkflowRetryRuleStatus.TIMED_OUT:
            return timed_out()
