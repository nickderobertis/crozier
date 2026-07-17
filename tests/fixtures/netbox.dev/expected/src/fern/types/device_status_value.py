

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeviceStatusValue(enum.StrEnum):
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
        if self is DeviceStatusValue.OFFLINE:
            return offline()
        if self is DeviceStatusValue.ACTIVE:
            return active()
        if self is DeviceStatusValue.PLANNED:
            return planned()
        if self is DeviceStatusValue.STAGED:
            return staged()
        if self is DeviceStatusValue.FAILED:
            return failed()
        if self is DeviceStatusValue.INVENTORY:
            return inventory()
        if self is DeviceStatusValue.DECOMMISSIONING:
            return decommissioning()
