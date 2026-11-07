

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SandboxEnvironmentVersionStatus(enum.StrEnum):
    """
    Readiness of the environment.
    """

    PENDING = "pending"
    READY = "ready"
    FAILED = "failed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        ready: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SandboxEnvironmentVersionStatus.PENDING:
            return pending()
        if self is SandboxEnvironmentVersionStatus.READY:
            return ready()
        if self is SandboxEnvironmentVersionStatus.FAILED:
            return failed()
