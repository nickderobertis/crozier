

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetJobsRequestStatus(enum.StrEnum):
    PROCESSING = "Processing"
    QUEUED = "Queued"
    COMPLETED = "Completed"
    FAILED = "Failed"

    def visit(
        self,
        processing: typing.Callable[[], T_Result],
        queued: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetJobsRequestStatus.PROCESSING:
            return processing()
        if self is GetJobsRequestStatus.QUEUED:
            return queued()
        if self is GetJobsRequestStatus.COMPLETED:
            return completed()
        if self is GetJobsRequestStatus.FAILED:
            return failed()
