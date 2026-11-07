

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunStatus(enum.StrEnum):
    """
    succeeded = all streams completed/skipped; failed = connection_status failed OR any stream errored.
    """

    STARTED = "started"
    SUCCEEDED = "succeeded"
    FAILED = "failed"

    def visit(
        self,
        started: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RunStatus.STARTED:
            return started()
        if self is RunStatus.SUCCEEDED:
            return succeeded()
        if self is RunStatus.FAILED:
            return failed()
