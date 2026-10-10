

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SandboxBuildStatus(enum.StrEnum):
    """
    Current build status.
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
        if self is SandboxBuildStatus.PENDING:
            return pending()
        if self is SandboxBuildStatus.READY:
            return ready()
        if self is SandboxBuildStatus.FAILED:
            return failed()
