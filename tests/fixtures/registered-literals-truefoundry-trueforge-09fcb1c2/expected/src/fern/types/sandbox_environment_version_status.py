

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SandboxEnvironmentVersionStatus(enum.StrEnum):
    """
    Readiness of the environment.
    """

    PENDING = "pending"
    ACTIVE = "active"
    FAILED = "failed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SandboxEnvironmentVersionStatus.PENDING:
            return pending()
        if self is SandboxEnvironmentVersionStatus.ACTIVE:
            return active()
        if self is SandboxEnvironmentVersionStatus.FAILED:
            return failed()
