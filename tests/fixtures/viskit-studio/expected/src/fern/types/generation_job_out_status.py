

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GenerationJobOutStatus(enum.StrEnum):
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
        if self is GenerationJobOutStatus.PLANNED:
            return planned()
        if self is GenerationJobOutStatus.QUEUED:
            return queued()
        if self is GenerationJobOutStatus.RUNNING:
            return running()
        if self is GenerationJobOutStatus.STOPPING:
            return stopping()
        if self is GenerationJobOutStatus.STOPPED:
            return stopped()
        if self is GenerationJobOutStatus.SUCCEEDED:
            return succeeded()
        if self is GenerationJobOutStatus.FAILED:
            return failed()
        if self is GenerationJobOutStatus.PARTIAL:
            return partial()
        if self is GenerationJobOutStatus.INTERRUPTED:
            return interrupted()
