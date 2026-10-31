

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobStatus(enum.StrEnum):
    """
    Durable job status. For batch parent jobs, status is derived from children after each
    child transition:
    1. If any child is non-terminal, the parent remains `queued` only while every child is
       queued; it becomes `running` once any child is running or terminal.
    2. When every child is terminal and any child is `indeterminate`, the parent is
       `indeterminate`.
    3. When every child is terminal, none are `indeterminate`, and any child is `failed`:
       the parent is `failed` if zero children succeeded, otherwise `succeeded` (mixed
       success/failure closes as parent `succeeded` while preserving failed children in
       summaries).
    4. When every child is `succeeded`, the parent is `succeeded`.

    Partial failures are always retained on child summaries; parent status does not drop
    failed children from results.
    """

    QUEUED = "queued"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    INDETERMINATE = "indeterminate"

    def visit(
        self,
        queued: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        indeterminate: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobStatus.QUEUED:
            return queued()
        if self is JobStatus.RUNNING:
            return running()
        if self is JobStatus.SUCCEEDED:
            return succeeded()
        if self is JobStatus.FAILED:
            return failed()
        if self is JobStatus.INDETERMINATE:
            return indeterminate()
