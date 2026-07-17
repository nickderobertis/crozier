

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WritableVirtualMachineWithConfigContextStatus(enum.StrEnum):
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
        if self is WritableVirtualMachineWithConfigContextStatus.OFFLINE:
            return offline()
        if self is WritableVirtualMachineWithConfigContextStatus.ACTIVE:
            return active()
        if self is WritableVirtualMachineWithConfigContextStatus.PLANNED:
            return planned()
        if self is WritableVirtualMachineWithConfigContextStatus.STAGED:
            return staged()
        if self is WritableVirtualMachineWithConfigContextStatus.FAILED:
            return failed()
        if self is WritableVirtualMachineWithConfigContextStatus.DECOMMISSIONING:
            return decommissioning()
