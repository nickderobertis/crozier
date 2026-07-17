

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VirtualMachineWithConfigContextStatusLabel(enum.StrEnum):
    OFFLINE = "Offline"
    ACTIVE = "Active"
    PLANNED = "Planned"
    STAGED = "Staged"
    FAILED = "Failed"
    DECOMMISSIONING = "Decommissioning"

    def visit(
        self,
        offline: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        planned: typing.Callable[[], T_Result],
        staged: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        decommissioning: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VirtualMachineWithConfigContextStatusLabel.OFFLINE:
            return offline()
        if self is VirtualMachineWithConfigContextStatusLabel.ACTIVE:
            return active()
        if self is VirtualMachineWithConfigContextStatusLabel.PLANNED:
            return planned()
        if self is VirtualMachineWithConfigContextStatusLabel.STAGED:
            return staged()
        if self is VirtualMachineWithConfigContextStatusLabel.FAILED:
            return failed()
        if self is VirtualMachineWithConfigContextStatusLabel.DECOMMISSIONING:
            return decommissioning()
