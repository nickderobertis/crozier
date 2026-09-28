

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V2TableJobStateStatus(enum.StrEnum):
    """
    Current background job state.
    """

    RUNNING = "running"
    READY = "ready"
    FAILED = "failed"
    CANCELED = "canceled"

    def visit(
        self,
        running: typing.Callable[[], T_Result],
        ready: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V2TableJobStateStatus.RUNNING:
            return running()
        if self is V2TableJobStateStatus.READY:
            return ready()
        if self is V2TableJobStateStatus.FAILED:
            return failed()
        if self is V2TableJobStateStatus.CANCELED:
            return canceled()
