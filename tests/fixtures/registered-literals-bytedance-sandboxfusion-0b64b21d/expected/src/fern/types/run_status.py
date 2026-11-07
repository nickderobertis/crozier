

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunStatus(enum.StrEnum):
    SUCCESS = "Success"
    FAILED = "Failed"
    SANDBOX_ERROR = "SandboxError"

    def visit(
        self,
        success: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        sandbox_error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RunStatus.SUCCESS:
            return success()
        if self is RunStatus.FAILED:
            return failed()
        if self is RunStatus.SANDBOX_ERROR:
            return sandbox_error()
