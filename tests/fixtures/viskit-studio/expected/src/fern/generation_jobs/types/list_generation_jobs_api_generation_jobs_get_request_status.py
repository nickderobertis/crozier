

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListGenerationJobsApiGenerationJobsGetRequestStatus(enum.StrEnum):
    PLANNED = "planned"
    QUEUED = "queued"
    RUNNING = "running"
    STOPPING = "stopping"
    STOPPED = "stopped"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    PARTIAL = "partial"
    INTERRUPTED = "interrupted"

    def visit(
        self,
        planned: typing.Callable[[], T_Result],
        queued: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        stopping: typing.Callable[[], T_Result],
        stopped: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        partial: typing.Callable[[], T_Result],
        interrupted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListGenerationJobsApiGenerationJobsGetRequestStatus.PLANNED:
            return planned()
        if self is ListGenerationJobsApiGenerationJobsGetRequestStatus.QUEUED:
            return queued()
        if self is ListGenerationJobsApiGenerationJobsGetRequestStatus.RUNNING:
            return running()
        if self is ListGenerationJobsApiGenerationJobsGetRequestStatus.STOPPING:
            return stopping()
        if self is ListGenerationJobsApiGenerationJobsGetRequestStatus.STOPPED:
            return stopped()
        if self is ListGenerationJobsApiGenerationJobsGetRequestStatus.SUCCEEDED:
            return succeeded()
        if self is ListGenerationJobsApiGenerationJobsGetRequestStatus.FAILED:
            return failed()
        if self is ListGenerationJobsApiGenerationJobsGetRequestStatus.PARTIAL:
            return partial()
        if self is ListGenerationJobsApiGenerationJobsGetRequestStatus.INTERRUPTED:
            return interrupted()
