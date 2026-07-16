

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class UpdateDagRunStateState(str, enum.Enum):
    """
    The state to set this DagRun
    """

    SUCCESS = "success"
    FAILED = "failed"
    QUEUED = "queued"

    def visit(
        self,
        success: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        queued: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdateDagRunStateState.SUCCESS:
            return success()
        if self is UpdateDagRunStateState.FAILED:
            return failed()
        if self is UpdateDagRunStateState.QUEUED:
            return queued()
