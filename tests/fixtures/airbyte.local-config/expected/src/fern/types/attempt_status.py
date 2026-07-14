

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AttemptStatus(str, enum.Enum):
    RUNNING = "running"
    FAILED = "failed"
    SUCCEEDED = "succeeded"

    def visit(
        self,
        running: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AttemptStatus.RUNNING:
            return running()
        if self is AttemptStatus.FAILED:
            return failed()
        if self is AttemptStatus.SUCCEEDED:
            return succeeded()
