

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetDeviceHealthLogRequestLogTypeItem(enum.StrEnum):
    BOOT = "boot"
    DFU_COMPLETED = "dfu_completed"

    def visit(self, boot: typing.Callable[[], T_Result], dfu_completed: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDeviceHealthLogRequestLogTypeItem.BOOT:
            return boot()
        if self is GetDeviceHealthLogRequestLogTypeItem.DFU_COMPLETED:
            return dfu_completed()
