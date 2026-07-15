

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DagState(str, enum.Enum):
    """
    DAG State.

    *Changed in version 2.1.3*&#58; 'queued' is added as a possible value.
    """

    QUEUED = "queued"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"

    def visit(
        self,
        queued: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        success: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DagState.QUEUED:
            return queued()
        if self is DagState.RUNNING:
            return running()
        if self is DagState.SUCCESS:
            return success()
        if self is DagState.FAILED:
            return failed()
