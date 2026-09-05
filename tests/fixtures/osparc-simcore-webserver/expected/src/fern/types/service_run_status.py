

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ServiceRunStatus(enum.StrEnum):
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"

    def visit(
        self,
        running: typing.Callable[[], T_Result],
        success: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ServiceRunStatus.RUNNING:
            return running()
        if self is ServiceRunStatus.SUCCESS:
            return success()
        if self is ServiceRunStatus.ERROR:
            return error()
