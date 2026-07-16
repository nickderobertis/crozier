

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ExecutionStatus(str, enum.Enum):
    UNAVAILABLE = "UNAVAILABLE"
    AVAILABLE = "AVAILABLE"
    EXECUTE_IN_PROGRESS = "EXECUTE_IN_PROGRESS"
    EXECUTE_COMPLETE = "EXECUTE_COMPLETE"
    EXECUTE_FAILED = "EXECUTE_FAILED"
    OBSOLETE = "OBSOLETE"

    def visit(
        self,
        unavailable: typing.Callable[[], T_Result],
        available: typing.Callable[[], T_Result],
        execute_in_progress: typing.Callable[[], T_Result],
        execute_complete: typing.Callable[[], T_Result],
        execute_failed: typing.Callable[[], T_Result],
        obsolete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExecutionStatus.UNAVAILABLE:
            return unavailable()
        if self is ExecutionStatus.AVAILABLE:
            return available()
        if self is ExecutionStatus.EXECUTE_IN_PROGRESS:
            return execute_in_progress()
        if self is ExecutionStatus.EXECUTE_COMPLETE:
            return execute_complete()
        if self is ExecutionStatus.EXECUTE_FAILED:
            return execute_failed()
        if self is ExecutionStatus.OBSOLETE:
            return obsolete()
