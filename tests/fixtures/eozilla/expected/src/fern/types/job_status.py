

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobStatus(enum.StrEnum):
    ACCEPTED = "accepted"
    RUNNING = "running"
    SUCCESSFUL = "successful"
    FAILED = "failed"
    DISMISSED = "dismissed"

    def visit(
        self,
        accepted: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        successful: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        dismissed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobStatus.ACCEPTED:
            return accepted()
        if self is JobStatus.RUNNING:
            return running()
        if self is JobStatus.SUCCESSFUL:
            return successful()
        if self is JobStatus.FAILED:
            return failed()
        if self is JobStatus.DISMISSED:
            return dismissed()
