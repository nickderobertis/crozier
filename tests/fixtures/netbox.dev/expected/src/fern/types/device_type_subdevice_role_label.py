

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DeviceTypeSubdeviceRoleLabel(str, enum.Enum):
    PARENT = "Parent"
    CHILD = "Child"

    def visit(self, parent: typing.Callable[[], T_Result], child: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeviceTypeSubdeviceRoleLabel.PARENT:
            return parent()
        if self is DeviceTypeSubdeviceRoleLabel.CHILD:
            return child()
