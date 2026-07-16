

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class VirtualMachineWithConfigContextStatusValue(str, enum.Enum):
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
        if self is VirtualMachineWithConfigContextStatusValue.OFFLINE:
            return offline()
        if self is VirtualMachineWithConfigContextStatusValue.ACTIVE:
            return active()
        if self is VirtualMachineWithConfigContextStatusValue.PLANNED:
            return planned()
        if self is VirtualMachineWithConfigContextStatusValue.STAGED:
            return staged()
        if self is VirtualMachineWithConfigContextStatusValue.FAILED:
            return failed()
        if self is VirtualMachineWithConfigContextStatusValue.DECOMMISSIONING:
            return decommissioning()
