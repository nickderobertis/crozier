

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EtcdKeyRotationStatusState(enum.StrEnum):
    """
    Whether the owned rotation is running, succeeded, or failed.
    """

    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"

    def visit(
        self,
        running: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EtcdKeyRotationStatusState.RUNNING:
            return running()
        if self is EtcdKeyRotationStatusState.SUCCEEDED:
            return succeeded()
        if self is EtcdKeyRotationStatusState.FAILED:
            return failed()
