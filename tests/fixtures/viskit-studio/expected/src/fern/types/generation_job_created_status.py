

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GenerationJobCreatedStatus(enum.StrEnum):
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
        if self is GenerationJobCreatedStatus.PLANNED:
            return planned()
        if self is GenerationJobCreatedStatus.QUEUED:
            return queued()
        if self is GenerationJobCreatedStatus.RUNNING:
            return running()
        if self is GenerationJobCreatedStatus.STOPPING:
            return stopping()
        if self is GenerationJobCreatedStatus.STOPPED:
            return stopped()
        if self is GenerationJobCreatedStatus.SUCCEEDED:
            return succeeded()
        if self is GenerationJobCreatedStatus.FAILED:
            return failed()
        if self is GenerationJobCreatedStatus.PARTIAL:
            return partial()
        if self is GenerationJobCreatedStatus.INTERRUPTED:
            return interrupted()
