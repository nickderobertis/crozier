

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WritableDeviceTypeSubdeviceRole(str, enum.Enum):
    """
    Parent devices house child devices in device bays. Leave blank if this device type is neither a parent nor a child.
    """

    PARENT = "parent"
    CHILD = "child"

    def visit(self, parent: typing.Callable[[], T_Result], child: typing.Callable[[], T_Result]) -> T_Result:
        if self is WritableDeviceTypeSubdeviceRole.PARENT:
            return parent()
        if self is WritableDeviceTypeSubdeviceRole.CHILD:
            return child()
