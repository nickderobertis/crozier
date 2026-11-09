

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BuildStatus(enum.StrEnum):
    CREATED = "created"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BuildStatus.CREATED:
            return created()
        if self is BuildStatus.RUNNING:
            return running()
        if self is BuildStatus.SUCCEEDED:
            return succeeded()
        if self is BuildStatus.FAILED:
            return failed()
