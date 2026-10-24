

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProviderSmokeTestStatus(enum.StrEnum):
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    BLOCKED = "blocked"

    def visit(
        self,
        running: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        blocked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProviderSmokeTestStatus.RUNNING:
            return running()
        if self is ProviderSmokeTestStatus.SUCCEEDED:
            return succeeded()
        if self is ProviderSmokeTestStatus.FAILED:
            return failed()
        if self is ProviderSmokeTestStatus.BLOCKED:
            return blocked()
