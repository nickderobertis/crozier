

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WritableModuleStatus(enum.StrEnum):
    OFFLINE = "offline"
    ACTIVE = "active"
    PLANNED = "planned"
    STAGED = "staged"
    FAILED = "failed"
    DECOMMISSIONING = "decommissioning"

    def visit(
        self,
        offline: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        planned: typing.Callable[[], T_Result],
        staged: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        decommissioning: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WritableModuleStatus.OFFLINE:
            return offline()
        if self is WritableModuleStatus.ACTIVE:
            return active()
        if self is WritableModuleStatus.PLANNED:
            return planned()
        if self is WritableModuleStatus.STAGED:
            return staged()
        if self is WritableModuleStatus.FAILED:
            return failed()
        if self is WritableModuleStatus.DECOMMISSIONING:
            return decommissioning()
