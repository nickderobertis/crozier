

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GenerationJobStopResponseStatus(enum.StrEnum):
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
        if self is GenerationJobStopResponseStatus.PLANNED:
            return planned()
        if self is GenerationJobStopResponseStatus.QUEUED:
            return queued()
        if self is GenerationJobStopResponseStatus.RUNNING:
            return running()
        if self is GenerationJobStopResponseStatus.STOPPING:
            return stopping()
        if self is GenerationJobStopResponseStatus.STOPPED:
            return stopped()
        if self is GenerationJobStopResponseStatus.SUCCEEDED:
            return succeeded()
        if self is GenerationJobStopResponseStatus.FAILED:
            return failed()
        if self is GenerationJobStopResponseStatus.PARTIAL:
            return partial()
        if self is GenerationJobStopResponseStatus.INTERRUPTED:
            return interrupted()
