

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WritableDeviceWithConfigContextStatus(str, enum.Enum):
    OFFLINE = "offline"
    ACTIVE = "active"
    PLANNED = "planned"
    STAGED = "staged"
    FAILED = "failed"
    INVENTORY = "inventory"
    DECOMMISSIONING = "decommissioning"

    def visit(
        self,
        offline: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        planned: typing.Callable[[], T_Result],
        staged: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        inventory: typing.Callable[[], T_Result],
        decommissioning: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WritableDeviceWithConfigContextStatus.OFFLINE:
            return offline()
        if self is WritableDeviceWithConfigContextStatus.ACTIVE:
            return active()
        if self is WritableDeviceWithConfigContextStatus.PLANNED:
            return planned()
        if self is WritableDeviceWithConfigContextStatus.STAGED:
            return staged()
        if self is WritableDeviceWithConfigContextStatus.FAILED:
            return failed()
        if self is WritableDeviceWithConfigContextStatus.INVENTORY:
            return inventory()
        if self is WritableDeviceWithConfigContextStatus.DECOMMISSIONING:
            return decommissioning()
