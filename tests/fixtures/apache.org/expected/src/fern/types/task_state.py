

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TaskState(str, enum.Enum):
    """
    Task state.

    *Changed in version 2.0.2*&#58; 'removed' is added as a possible value.

    *Changed in version 2.2.0*&#58; 'deferred' is added as a possible value.

    *Changed in version 2.4.0*&#58; 'sensing' state has been removed.
    *Changed in version 2.4.2*&#58; 'restarting' is added as a possible value
    """

    SUCCESS = "success"
    RUNNING = "running"
    FAILED = "failed"
    UPSTREAM_FAILED = "upstream_failed"
    SKIPPED = "skipped"
    UP_FOR_RETRY = "up_for_retry"
    UP_FOR_RESCHEDULE = "up_for_reschedule"
    QUEUED = "queued"
    NONE = "none"
    SCHEDULED = "scheduled"
    DEFERRED = "deferred"
    REMOVED = "removed"
    RESTARTING = "restarting"

    def visit(
        self,
        success: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        upstream_failed: typing.Callable[[], T_Result],
        skipped: typing.Callable[[], T_Result],
        up_for_retry: typing.Callable[[], T_Result],
        up_for_reschedule: typing.Callable[[], T_Result],
        queued: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
        scheduled: typing.Callable[[], T_Result],
        deferred: typing.Callable[[], T_Result],
        removed: typing.Callable[[], T_Result],
        restarting: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TaskState.SUCCESS:
            return success()
        if self is TaskState.RUNNING:
            return running()
        if self is TaskState.FAILED:
            return failed()
        if self is TaskState.UPSTREAM_FAILED:
            return upstream_failed()
        if self is TaskState.SKIPPED:
            return skipped()
        if self is TaskState.UP_FOR_RETRY:
            return up_for_retry()
        if self is TaskState.UP_FOR_RESCHEDULE:
            return up_for_reschedule()
        if self is TaskState.QUEUED:
            return queued()
        if self is TaskState.NONE:
            return none()
        if self is TaskState.SCHEDULED:
            return scheduled()
        if self is TaskState.DEFERRED:
            return deferred()
        if self is TaskState.REMOVED:
            return removed()
        if self is TaskState.RESTARTING:
            return restarting()
