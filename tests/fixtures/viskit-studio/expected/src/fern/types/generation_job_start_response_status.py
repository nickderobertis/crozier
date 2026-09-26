

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GenerationJobStartResponseStatus(enum.StrEnum):
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
        if self is GenerationJobStartResponseStatus.PLANNED:
            return planned()
        if self is GenerationJobStartResponseStatus.QUEUED:
            return queued()
        if self is GenerationJobStartResponseStatus.RUNNING:
            return running()
        if self is GenerationJobStartResponseStatus.STOPPING:
            return stopping()
        if self is GenerationJobStartResponseStatus.STOPPED:
            return stopped()
        if self is GenerationJobStartResponseStatus.SUCCEEDED:
            return succeeded()
        if self is GenerationJobStartResponseStatus.FAILED:
            return failed()
        if self is GenerationJobStartResponseStatus.PARTIAL:
            return partial()
        if self is GenerationJobStartResponseStatus.INTERRUPTED:
            return interrupted()
