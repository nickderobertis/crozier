

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeviceWithConfigContextStatusLabel(enum.StrEnum):
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
        if self is DeviceWithConfigContextStatusLabel.OFFLINE:
            return offline()
        if self is DeviceWithConfigContextStatusLabel.ACTIVE:
            return active()
        if self is DeviceWithConfigContextStatusLabel.PLANNED:
            return planned()
        if self is DeviceWithConfigContextStatusLabel.STAGED:
            return staged()
        if self is DeviceWithConfigContextStatusLabel.FAILED:
            return failed()
        if self is DeviceWithConfigContextStatusLabel.INVENTORY:
            return inventory()
        if self is DeviceWithConfigContextStatusLabel.DECOMMISSIONING:
            return decommissioning()
