

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WorkflowGetJobsResponseItemsItemStatus(enum.StrEnum):
    """
    The current status of the job.
    """

    SUCCESS = "success"
    RUNNING = "running"
    NOT_RUN = "not_run"
    FAILED = "failed"
    RETRIED = "retried"
    QUEUED = "queued"
    NOT_RUNNING = "not_running"
    INFRASTRUCTURE_FAIL = "infrastructure_fail"
    TIMEDOUT = "timedout"
    ON_HOLD = "on_hold"
    TERMINATED_UNKNOWN = "terminated-unknown"
    BLOCKED = "blocked"
    CANCELED = "canceled"
    UNAUTHORIZED = "unauthorized"

    def visit(
        self,
        success: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        not_run: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        retried: typing.Callable[[], T_Result],
        queued: typing.Callable[[], T_Result],
        not_running: typing.Callable[[], T_Result],
        infrastructure_fail: typing.Callable[[], T_Result],
        timedout: typing.Callable[[], T_Result],
        on_hold: typing.Callable[[], T_Result],
        terminated_unknown: typing.Callable[[], T_Result],
        blocked: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        unauthorized: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WorkflowGetJobsResponseItemsItemStatus.SUCCESS:
            return success()
        if self is WorkflowGetJobsResponseItemsItemStatus.RUNNING:
            return running()
        if self is WorkflowGetJobsResponseItemsItemStatus.NOT_RUN:
            return not_run()
        if self is WorkflowGetJobsResponseItemsItemStatus.FAILED:
            return failed()
        if self is WorkflowGetJobsResponseItemsItemStatus.RETRIED:
            return retried()
        if self is WorkflowGetJobsResponseItemsItemStatus.QUEUED:
            return queued()
        if self is WorkflowGetJobsResponseItemsItemStatus.NOT_RUNNING:
            return not_running()
        if self is WorkflowGetJobsResponseItemsItemStatus.INFRASTRUCTURE_FAIL:
            return infrastructure_fail()
        if self is WorkflowGetJobsResponseItemsItemStatus.TIMEDOUT:
            return timedout()
        if self is WorkflowGetJobsResponseItemsItemStatus.ON_HOLD:
            return on_hold()
        if self is WorkflowGetJobsResponseItemsItemStatus.TERMINATED_UNKNOWN:
            return terminated_unknown()
        if self is WorkflowGetJobsResponseItemsItemStatus.BLOCKED:
            return blocked()
        if self is WorkflowGetJobsResponseItemsItemStatus.CANCELED:
            return canceled()
        if self is WorkflowGetJobsResponseItemsItemStatus.UNAUTHORIZED:
            return unauthorized()
