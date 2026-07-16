

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeviceStatusLabel(enum.StrEnum):
    OFFLINE = "Offline"
    ACTIVE = "Active"
    PLANNED = "Planned"
    STAGED = "Staged"
    FAILED = "Failed"
    INVENTORY = "Inventory"
    DECOMMISSIONING = "Decommissioning"

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
        if self is DeviceStatusLabel.OFFLINE:
            return offline()
        if self is DeviceStatusLabel.ACTIVE:
            return active()
        if self is DeviceStatusLabel.PLANNED:
            return planned()
        if self is DeviceStatusLabel.STAGED:
            return staged()
        if self is DeviceStatusLabel.FAILED:
            return failed()
        if self is DeviceStatusLabel.INVENTORY:
            return inventory()
        if self is DeviceStatusLabel.DECOMMISSIONING:
            return decommissioning()
