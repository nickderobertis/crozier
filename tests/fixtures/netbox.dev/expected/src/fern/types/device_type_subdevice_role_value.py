

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeviceTypeSubdeviceRoleValue(enum.StrEnum):
    PARENT = "parent"
    CHILD = "child"

    def visit(self, parent: typing.Callable[[], T_Result], child: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeviceTypeSubdeviceRoleValue.PARENT:
            return parent()
        if self is DeviceTypeSubdeviceRoleValue.CHILD:
            return child()
