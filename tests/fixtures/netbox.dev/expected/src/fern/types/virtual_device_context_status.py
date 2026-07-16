

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class VirtualDeviceContextStatus(str, enum.Enum):
    ACTIVE = "active"
    PLANNED = "planned"
    OFFLINE = "offline"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        planned: typing.Callable[[], T_Result],
        offline: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VirtualDeviceContextStatus.ACTIVE:
            return active()
        if self is VirtualDeviceContextStatus.PLANNED:
            return planned()
        if self is VirtualDeviceContextStatus.OFFLINE:
            return offline()
