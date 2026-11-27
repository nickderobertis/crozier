

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReviewSnapshotStatus(enum.StrEnum):
    """
    the current status of the Snapshot process
    """

    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReviewSnapshotStatus.PENDING:
            return pending()
        if self is ReviewSnapshotStatus.RUNNING:
            return running()
        if self is ReviewSnapshotStatus.SUCCEEDED:
            return succeeded()
        if self is ReviewSnapshotStatus.FAILED:
            return failed()
