

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WritableVirtualDeviceContextStatus(str, enum.Enum):
    ACTIVE = "active"
    PLANNED = "planned"
    OFFLINE = "offline"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        planned: typing.Callable[[], T_Result],
        offline: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WritableVirtualDeviceContextStatus.ACTIVE:
            return active()
        if self is WritableVirtualDeviceContextStatus.PLANNED:
            return planned()
        if self is WritableVirtualDeviceContextStatus.OFFLINE:
            return offline()
