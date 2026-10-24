

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReportSyncStatus(enum.StrEnum):
    QUEUED = "queued"
    POLLING = "polling"
    SUCCEEDED = "succeeded"
    FAILED = "failed"

    def visit(
        self,
        queued: typing.Callable[[], T_Result],
        polling: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReportSyncStatus.QUEUED:
            return queued()
        if self is ReportSyncStatus.POLLING:
            return polling()
        if self is ReportSyncStatus.SUCCEEDED:
            return succeeded()
        if self is ReportSyncStatus.FAILED:
            return failed()
