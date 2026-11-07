

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAllJobsRequestStatus(enum.StrEnum):
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
        if self is GetAllJobsRequestStatus.PROCESSING:
            return processing()
        if self is GetAllJobsRequestStatus.QUEUED:
            return queued()
        if self is GetAllJobsRequestStatus.COMPLETED:
            return completed()
        if self is GetAllJobsRequestStatus.FAILED:
            return failed()
