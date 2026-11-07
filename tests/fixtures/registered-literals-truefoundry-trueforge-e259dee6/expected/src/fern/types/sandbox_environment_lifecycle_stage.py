

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SandboxEnvironmentLifecycleStage(enum.StrEnum):
    """
    Soft-delete lifecycle stage.
    """

    ACTIVE = "active"
    DELETED = "deleted"

    def visit(self, active: typing.Callable[[], T_Result], deleted: typing.Callable[[], T_Result]) -> T_Result:
        if self is SandboxEnvironmentLifecycleStage.ACTIVE:
            return active()
        if self is SandboxEnvironmentLifecycleStage.DELETED:
            return deleted()
